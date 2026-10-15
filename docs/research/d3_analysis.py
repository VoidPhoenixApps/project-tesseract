"""D3 parametric desk calculations, SI except explicitly named mm/deg quantities.

No vendor geometry, physical acceptance limits, hardware or external dependencies.
Run with Python 3.9+ from any directory; stdout is deterministic JSON.
"""
import importlib.util
import json
from math import hypot, isfinite, pi, radians, tan
from pathlib import Path

from d1_analysis import G, angular_error_mm, lift
from d2_geometry import MODES

spec = importlib.util.spec_from_file_location(
    'd3_phase1b', Path(__file__).resolve().parents[1] / 'phase1b' / 'analysis.py')
thermal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(thermal)


def finite(*values):
    if not all(isfinite(v) for v in values):
        raise ValueError('finite inputs required')


def positive(*values):
    finite(*values)
    if any(v <= 0 for v in values):
        raise ValueError('positive inputs required')


def nonnegative(*values):
    finite(*values)
    if any(v < 0 for v in values):
        raise ValueError('nonnegative inputs required')


def group_loads(mode, masses, extra_mass=0):
    """Masses keyed by bed ID; extra mass per group, not per module."""
    if mode not in MODES or set(masses) != {1, 2, 3, 4}:
        raise ValueError('known mode and four bed masses required')
    positive(*masses.values())
    nonnegative(extra_mass)
    return [{'beds': list(group), 'mass_kg': sum(masses[i] for i in group)+extra_mass,
             **lift(sum(masses[i] for i in group)+extra_mass)} for group in MODES[mode]]


def reactions(force_n, spacing_mm, eccentricity_mm):
    """Two support lines at +/- spacing/2; negative reaction means hold-down needed."""
    positive(force_n, spacing_mm)
    finite(eccentricity_mm)
    return (force_n*(.5-eccentricity_mm/spacing_mm),
            force_n*(.5+eccentricity_mm/spacing_mm))


def tripod(force_n, points, com):
    """Three vertical point reactions from force and two moment balances, no clamping."""
    positive(force_n)
    if len(points) != 3 or len(com) != 2 or any(len(p) != 2 for p in points):
        raise ValueError('three XY supports and XY center of mass required')
    finite(*com, *(x for p in points for x in p))
    (x1, y1), (x2, y2), (x3, y3) = points
    den = (y2-y3)*(x1-x3)+(x3-x2)*(y1-y3)
    if abs(den) < 1e-12:
        raise ValueError('collinear supports')
    a = ((y2-y3)*(com[0]-x3)+(x3-x2)*(com[1]-y3))/den
    b = ((y3-y1)*(com[0]-x3)+(x1-x3)*(com[1]-y3))/den
    return tuple(force_n*w for w in (a, b, 1-a-b))


def cantilever(force_n, length_mm, ei_n_mm2):
    """Ideal small-deflection prismatic arm with tip load, not a cross-frame solver."""
    nonnegative(force_n, length_mm)
    positive(ei_n_mm2)
    return {'root_moment_nm': force_n*length_mm/1000,
            'tip_deflection_mm': force_n*length_mm**3/(3*ei_n_mm2)}


def guide_loop(travel_mm, angle_deg, initial_mm, free_mm, stiffness_n_mm):
    nonnegative(travel_mm, free_mm)
    positive(stiffness_n_mm)
    finite(angle_deg, initial_mm)
    if abs(angle_deg) >= 90:
        raise ValueError('angle outside small-slope model domain')
    mismatch = initial_mm+travel_mm*tan(radians(angle_deg))
    return {'mismatch_mm': mismatch,
            'elastic_force_n': max(0, abs(mismatch)-free_mm)*stiffness_n_mm}


def selector_span(half_span_mm, offset_mm, tension_n):
    """Zero-radius movable point between fixed endpoints; a counterexample, not belt CAD.

    Return path length, slope and ideal selector reaction at uniform imposed tension.
    """
    positive(half_span_mm)
    finite(offset_mm)
    nonnegative(tension_n)
    slope = 2*offset_mm/hypot(half_span_mm, offset_mm)
    return {'length_mm': 2*hypot(half_span_mm, offset_mm),
            'dlength_doffset': slope, 'selector_force_n': tension_n*slope}


def backlash_mm(upstream_deg, output_deg, travel_mm_rev, reduction):
    nonnegative(upstream_deg, output_deg)
    positive(travel_mm_rev, reduction)
    return angular_error_mm(upstream_deg/reduction+output_deg, travel_mm_rev)


def seam_budget(dz_mm, slopes_a, slopes_b, local_a, local_b, terms):
    """Worst-sign vertical error magnitudes; slopes are Rx/Ry radians (small angle).

    local coordinates measured from each plate's own reference. No RSS or probability.
    terms must not duplicate effects already included in slopes or dz.
    """
    for pair in (slopes_a, slopes_b, local_a, local_b):
        if len(pair) != 2:
            raise ValueError('pairs required')
        finite(*pair)
    nonnegative(dz_mm, *terms.values())
    tilt = sum(abs(rx*y)+abs(ry*x) for (rx, ry), (x, y) in
               ((slopes_a, local_a), (slopes_b, local_b)))
    return {'drive_mm': dz_mm, 'tilt_mm': tilt, **terms,
            'total_mm': dz_mm+tilt+sum(terms.values())}


def arrest(mass_kg, downward_speed_m_s, delay_s, stopping_stroke_mm):
    """Free fall during delay, then energy-average catch force; not peak or safe rating."""
    positive(mass_kg, stopping_stroke_mm)
    nonnegative(downward_speed_m_s, delay_s)
    d = downward_speed_m_s*delay_s+.5*G*delay_s**2
    v = downward_speed_m_s+G*delay_s
    s = stopping_stroke_mm/1000
    energy = .5*mass_kg*v*v+mass_kg*G*s
    return {'precatch_drop_mm': d*1000, 'catch_speed_m_s': v,
            'absorbed_energy_j': energy, 'average_catch_force_n': energy/s,
            'total_drop_mm': d*1000+stopping_stroke_mm}


def graph_groups(edges):
    """Scalar Z-equality graph only; says nothing about six-DOF structural stability."""
    groups = [{i} for i in range(1, 5)]
    for a, b in edges:
        if a == b or a not in range(1, 5) or b not in range(1, 5):
            raise ValueError('distinct valid beds required')
        ga, gb = next(g for g in groups if a in g), next(g for g in groups if b in g)
        if ga is not gb:
            groups = [g for g in groups if g is not ga and g is not gb]+[ga | gb]
    return sorted(tuple(sorted(g)) for g in groups)


def results():
    masses = {1: 1., 2: 2., 3: 3., 4: 4.}  # hypothetical includes carried parts
    f = 12*G
    span = [dict(q_mm=q, **selector_span(100, q, 50)) for q in (-20, -10, 0, 10, 20)]
    return {
        'status': 'Analytical sensitivities, not geometry, ratings or physical validation',
        'assumed_masses_kg': masses,
        'modes': {mode: group_loads(mode, masses) for mode in MODES},
        'J_frame_mass_sweep': [dict(frame_kg=m, **lift(10+m)) for m in (0, 2, 4)],
        '12kg_reactions_spacing_240mm': {str(e): reactions(f, 240, e) for e in (0, 60, 150)},
        '12kg_tripod_120mm': {str(com): tripod(f, ((-120, -120), (120, -120), (0, 120)), com)
                             for com in ((0, 0), (90, 90))},
        'arm_20N_90mm': {str(ei): cantilever(20, 90, ei) for ei in (1e6, 1e7, 1e8)},
        'guide_loop_200mm_1000N_mm': {str(a): guide_loop(200, a, .02, .05, 1000)
                                   for a in (.01, .05, .1)},
        'selector_counterexample': span,
        'selector_length_excursion_mm': max(x['length_mm'] for x in span)-min(x['length_mm'] for x in span),
        'backlash_1deg_each_3to1_belt40_mm': backlash_mm(1, 1, 40, 3),
        'seam_example': seam_budget(.02, (.0001, .0001), (.0001, .0001),
                                   (90, 90), (-90, 90),
                                   {'elastic_mm': .02, 'thermal_residual_mm': .02,
                                    'sheet_mm': .02, 'engagement_mm': .01, 'measurement_guard_mm': .01}),
        'thermal_reused': {'center_cold_interval_mm': thermal.cold_interval('center'),
                           'inset10_cold_interval_mm': thermal.cold_interval('inset'),
                           'center_hot_gap_mm': thermal.gap(100, 100),
                           'inset10_hot_gap_mm': thermal.gap(100, 100, 'inset')},
        '12kg_arrest_0p01m_s_1mm_stroke': {str(t): arrest(12, .01, t/1000, 1) for t in (10, 20, 50)},
        'z_graphs': {'two_rows': graph_groups(((1, 2), (3, 4))),
                     'two_columns': graph_groups(((1, 3), (2, 4))),
                     'joined_tree': graph_groups(((1, 2), (1, 3), (3, 4))),
                     'unified_frame': graph_groups(((1, 2), (1, 3), (2, 4), (3, 4)))},
    }


if __name__ == '__main__':
    print(json.dumps(results(), indent=2, sort_keys=True))
