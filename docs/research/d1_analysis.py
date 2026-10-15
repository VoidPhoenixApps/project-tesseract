"""D1 analytical sensitivities; standard library, no machine or CAD interfaces.

Run: python3 -B docs/research/d1_analysis.py
Inputs are hypothetical study parameters, never component ratings or limits.
"""
from math import isfinite, pi, radians, tan
import json

G = 9.80665


def positive(*values):
    if any(not isfinite(v) or v <= 0 for v in values):
        raise ValueError('expected finite positive inputs')


def lift(mass_kg, radius_mm=6.366197723675814, lead_mm=8,
         efficiency=0.7, reduction=1, advantage=1, acceleration=0, drag_n=0):
    """reduction=motor turns/output turn; advantage=belt travel/lift travel.

    Force includes upward acceleration and aggregate opposing drag. Screw
    result uses reduction but no belt reeving advantage. Excludes rotary inertia.
    """
    positive(mass_kg, radius_mm, lead_mm, efficiency, reduction, advantage)
    if efficiency > 1 or not all(isfinite(v) and v >= 0 for v in (acceleration, drag_n)):
        raise ValueError('invalid efficiency, acceleration or drag')
    force = mass_kg * (G + acceleration) + drag_n
    return {'force_n': force, 'belt_tension_difference_n': force / advantage,
            'belt_motor_nm': force * radius_mm / 1000 / (efficiency * reduction * advantage),
            'screw_motor_nm': force * lead_mm / 1000 / (2*pi*efficiency*reduction)}


def common_z_interval(heights, strokes, gantry_limits):
    """h_i=g+q_i; q_i in (lo,hi). Return intersection or None, all mm."""
    if not heights or len(heights) != len(strokes):
        raise ValueError('one stroke interval per nonempty height vector')
    intervals = [gantry_limits] + list(strokes)
    if any(len(x) != 2 or not all(isfinite(v) for v in x) or x[0] > x[1] for x in intervals):
        raise ValueError('invalid interval')
    if not all(isfinite(h) for h in heights):
        raise ValueError('invalid heights')
    lo = max([gantry_limits[0]] + [h-s[1] for h, s in zip(heights, strokes)])
    hi = min([gantry_limits[1]] + [h-s[0] for h, s in zip(heights, strokes)])
    return (lo, hi) if lo <= hi else None


def seam_step(drive_mm, lever_mm, tilt_deg, differential_load_n, stiffness_n_mm,
              thermal_mm=0, sheet_mm=0, engagement_mm=0):
    """Worst-sign bound; excludes correlation/probability claims."""
    positive(stiffness_n_mm)
    values = (drive_mm, lever_mm, tilt_deg, differential_load_n, thermal_mm, sheet_mm, engagement_mm)
    if not all(isfinite(v) and v >= 0 for v in values) or tilt_deg >= 90:
        raise ValueError('invalid nonnegative error magnitudes')
    return (drive_mm + lever_mm*tan(radians(tilt_deg)) + differential_load_n/stiffness_n_mm
            + thermal_mm + sheet_mm + engagement_mm)


def angular_error_mm(degrees, travel_per_rev_mm):
    positive(travel_per_rev_mm)
    if not isfinite(degrees):
        raise ValueError('invalid angle')
    return degrees / 360 * travel_per_rev_mm


def aabb(bounds):
    if len(bounds) != 6 or not all(isfinite(v) for v in bounds):
        raise ValueError('expected finite xmin,xmax,ymin,ymax,zmin,zmax')
    if any(bounds[i] > bounds[i+1] for i in (0, 2, 4)):
        raise ValueError('inverted box')
    return tuple(bounds)


def sweep_box(local, start, end):
    """Conservative swept AABB for fixed-orientation straight translation only."""
    aabb(local)
    if len(start) != 3 or len(end) != 3 or not all(isfinite(x) for x in (*start, *end)):
        raise ValueError('invalid endpoints')
    return tuple(v for i in range(3) for v in
                 (local[2*i]+min(start[i], end[i]), local[2*i+1]+max(start[i], end[i])))


def overlaps(a, b, clearance=0):
    """Touching is conservatively a conflict. AABB overlap is not exact contact."""
    aabb(a); aabb(b)
    if not isfinite(clearance) or clearance < 0:
        raise ValueError('invalid clearance')
    return not any(a[i+1]+clearance < b[i] or b[i+1]+clearance < a[i] for i in (0, 2, 4))


def results():
    return {
        'evidence': 'Hypothetical analytical sensitivity; not validation or selection',
        'plate_mass_kg_180mm_square_2700kg_m3': {str(t): .18**2*(t/1000)*2700 for t in (3,4,6)},
        'lift_static_nominal': {str(m): lift(m) for m in (1,2,4,8,16)},
        'lift_16kg_sensitivity': [dict(efficiency=e, reduction=r, **lift(16, efficiency=e, reduction=r))
                                for e in (.3,.7,.9) for r in (1,3)],
        'thermal_mm': {'al_180_80K': 23.6e-6*180*80, 'inset10_pair_80K': 23.6e-6*20*80,
                       'steel_cross_360_20K': 12e-6*360*20},
        'tilt_edge_mm_90lever': {str(a): 90*tan(radians(a)) for a in (.01,.05,.1)},
        'compliance_mm_10N': {str(k): 10/k for k in (100,500,2000)},
        'seam_example_mm': seam_step(.02,90,.05,10,500,.02,.02,.01),
        'engagement_1deg_mm': {'8mm_screw': angular_error_mm(1,8),
                               '40mm_belt': angular_error_mm(1,40)},
        'free_fall_from_rest_mm': {str(t): .5*G*(t/1000)**2*1000 for t in (10,20,50)},
        'short_stroke_intervals_mm': {str(h): common_z_interval((0,h), ((-10,10),)*2, (-300,300))
                                      for h in (10,20,21,100)},
        'head_sweep_conflict_tall_object': overlaps(
            sweep_box((-35,15,-25,25,5,65),(-80,0,10),(80,0,10)), (0,20,-10,10,0,80)),
        'head_sweep_conflict_low_object': overlaps(
            sweep_box((-35,15,-25,25,5,65),(-80,0,10),(80,0,10)), (0,20,-10,10,0,5)),
    }


if __name__ == '__main__':
    print(json.dumps(results(), indent=2, sort_keys=True))
