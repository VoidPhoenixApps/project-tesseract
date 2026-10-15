"""D4 bounded structural sensitivities. Python 3.9+, standard library, SI units.

Abstract members and springs, not manufacturer geometry, FEA or capacity ratings.
See d4-calculations.md for derivations, sources and excluded behavior.
"""
import json
from math import hypot, isfinite, pi, sqrt
from d2_geometry import MODES
from d3_analysis import guide_loop, reactions


def positive(*xs):
    if any(not isfinite(x) or x <= 0 for x in xs):
        raise ValueError('finite positive values required')


def nonnegative(*xs):
    if any(not isfinite(x) or x < 0 for x in xs):
        raise ValueError('finite nonnegative values required')


def circular(od, wall=None):
    positive(od)
    if wall is None:
        inner = 0
    else:
        positive(wall)
        if 2*wall >= od:
            raise ValueError('tube requires a positive bore; use wall=None for solid')
        inner = od-2*wall
    area = pi*(od**2-inner**2)/4
    inertia = pi*(od**4-inner**4)/64
    return area, inertia


def beam(force, length, modulus, inertia, support='cantilever'):
    nonnegative(force)
    positive(length, modulus, inertia)
    if support not in ('cantilever', 'simple_center'):
        raise ValueError('unsupported boundary condition')
    divisor = 3 if support == 'cantilever' else 48
    return force*length**3/(divisor*modulus*inertia)


def arm(force, length, modulus, inertia, root_k):
    """Tip load, elastic root rotation; no slip, shear or local contact deformation."""
    positive(root_k)
    return {'moment_nm': force*length,
            'member_mm': 1000*beam(force, length, modulus, inertia),
            'root_mm': 1000*force*length**2/root_k,
            'total_mm': 1000*(beam(force, length, modulus, inertia)
                             + force*length**2/root_k)}


def buckling(modulus, inertia, length, end_factor=1):
    positive(modulus, inertia, length, end_factor)
    return pi*pi*modulus*inertia/(end_factor*length)**2


def v_truss(force, half_span, height, modulus, area, inertia, joint_k):
    """Two identical compression struts, fixed feet (+/-b,0), apex (0,h).

    joint_k is axial stiffness of EACH end joint. In-plane vertical load only.
    Out-of-plane apex restraint is assumed, not provided by these two bars.
    """
    nonnegative(force)
    positive(half_span, height, modulus, area, inertia, joint_k)
    length = hypot(half_span, height)
    sin_angle = height/length
    bar_k = 1/(length/(modulus*area)+2/joint_k)
    k_vertical = 2*bar_k*sin_angle**2
    displacement = force/k_vertical
    # A diagnostic threshold only: values below it are NOT validated.
    return {'length_m': length, 'compression_n': force/(2*sin_angle),
            'linear_deflection_over_rise': displacement/height,
            'large_displacement_warning': displacement/height >= .1,
            'K2_euler_demand_exceeded': force/(2*sin_angle) >= buckling(modulus, inertia, length, 2),
            'vertical_stiffness_n_m': k_vertical, 'deflection_mm': 1000*force/k_vertical,
            'euler_n_K1': buckling(modulus, inertia, length),
            'euler_n_K2': buckling(modulus, inertia, length, 2)}


def bay_torsion(torque, width, side_k):
    """Rigid crossbar on two lateral springs separated by width; no translation."""
    nonnegative(torque)
    positive(width, side_k)
    ktheta = side_k*width**2/2
    return {'ktheta_nm_rad': ktheta, 'angle_rad': torque/ktheta,
            'edge_motion_mm': 1000*torque/ktheta*width/2}


def pair_support(f1, f2, k1, k2, tie_k, datum2=0):
    """Downward displacement; second support rest coordinate datum2.

    Two grounded springs plus a relative vertical tie; no rotations or capacity.
    Zero k represents loss of a path, not a valid operating permission.
    """
    nonnegative(f1, f2, k1, k2, tie_k)
    if not isfinite(datum2):
        raise ValueError('finite datum required')
    determinant = k1*k2+tie_k*(k1+k2)
    if determinant <= 0:
        raise ValueError('no stable two-coordinate support')
    rhs2 = f2+k2*datum2
    u1 = ((k2+tie_k)*f1+tie_k*rhs2)/determinant
    u2 = (tie_k*f1+(k1+tie_k)*rhs2)/determinant
    return {'u1_mm': 1000*u1, 'u2_mm': 1000*u2,
            'relative_mm': 1000*(u2-u1),
            'support1_n': k1*u1, 'support2_n': k2*(u2-datum2),
            'tie_on_1_down_n': tie_k*(u2-u1)}


def mode_graph(mode):
    """Explicit independent L paths; optional group P/T/L trees are distinct labels."""
    if mode not in MODES:
        raise ValueError('unknown mode')
    groups = MODES[mode]
    edges = []
    for group in groups:
        # Adjacent bed tree: avoid diagonal ties in J.
        allowed = [(1, 2), (1, 3), (3, 4), (2, 4)]
        reached = {group[0]}
        while len(reached) < len(group):
            for a, b in allowed:
                if a in group and b in group and ((a in reached) != (b in reached)):
                    edges.append([a, b])
                    reached.update((a, b))
                    break
            else:
                raise ValueError('group has no adjacent tree')
    return {'groups': [list(g) for g in groups], 'progress_coordinates': len(groups),
            'L_independent': [[f'bed{i}', f'lift{i}', 'frame'] for i in range(1, 5)],
            'P_alternative_released_tree': edges,
            'T_optional_selected_tree': [e[:] for e in edges],
            'L_optional_hybrid_ties': [e[:] for e in edges],
            'unified_platform_attached_compatible': len(groups) == 1}


def results():
    steel_e, steel_rho = 210e9, 7850
    sections = {}
    for name, od, wall in [('metric_shaft_12', .012, None),
                           ('inch_shaft_half_nominal', .0127, None),
                           ('metric_tube_25x1p5', .025, .0015),
                           ('metric_tube_25x2', .025, .002),
                           ('inch_tube_1x065', .0254, .001651)]:
        a, i = circular(od, wall)
        sections[name] = {'area_mm2': a*1e6, 'I_mm4': i*1e12,
                         'mass_kg_m': a*steel_rho,
                         'center_100N_600mm_deflection_mm': 1000*beam(100, .6, steel_e, i, 'simple_center'),
                         'arm_20N_300mm_root_10000Nm_rad': arm(20, .3, steel_e, i, 10000)}
    sections['2020_reference'] = {
        'I_mm4': 6826, 'E_assumed_pa': 69e9,
        'center_100N_600mm_deflection_mm': 1000*beam(100, .6, 69e9, 6826e-12, 'simple_center'),
        'arm_20N_300mm_root_10000Nm_rad': arm(20, .3, 69e9, 6826e-12, 10000)}
    # Hypothetical SOLID square printed bars; not infill-equivalent sections.
    a, i = .02**2, .02**4/12
    trusses = [{'height_m': h, 'E_pa': e, 'joint_k_n_m': j,
                **v_truss(100, .3, h, e, a, i, j)}
               for h in (.05, .15, .3) for e in (.5e9, 2e9)
               for j in (1e5, 1e6, 1e7)]
    _, tube_i = circular(.025, .0015)
    roots = [{'root_k_nm_rad': k, **arm(20, .3, steel_e, tube_i, k)}
             for k in (1e3, 1e4, 1e5)]
    pairs = {name: pair_support(20, 40, k1, k2, tie, offset)
             for name, k1, k2, tie, offset in [
                 ('independent', 1e6, 1e6, 0, 0),
                 ('hybrid', 1e6, 1e6, 1e6, 0),
                 ('hybrid_mismatch_0p2mm', 1e6, 1e6, 1e6, .0002),
                 ('support2_lost_tie_present', 1e6, 0, 1e6, 0)]}
    return {'status': 'Hypothetical desk sensitivities; no ratings or physical validation',
            'sections': sections, 'printed_v_trusses': trusses, 'root_sensitivity': roots,
            'torsion': [{'side_k_n_m': k, **bay_torsion(10, .6, k)} for k in (1e4, 1e5, 1e6)],
            'pair_support': pairs,
            'eccentric_100N_240mm': {str(e): list(reactions(100, 240, e)) for e in (0, 60, 150)},
            'guide': [guide_loop(200, angle, .02, .05, 1000) for angle in (.01, .05, .1)],
            'thermal': {'steel_alpha_assumed_per_K': 12e-6, 'al_alpha_per_K': 23.6e-6,
                        '600mm_20K_steel_mm': 12e-6*600*20,
                        '600mm_20K_al_mm': 23.6e-6*600*20,
                        'steel_600mm_5K_differential_mm': 12e-6*600*5},
            'frequency': [{'k_n_m': k, 'mass_kg': m, 'hz': sqrt(k/m)/(2*pi)}
                          for k in (1e4, 1e5, 1e6) for m in (2, 10, 20)],
            'modes': {mode: mode_graph(mode) for mode in MODES}}


if __name__ == '__main__':
    print(json.dumps(results(), indent=2, sort_keys=True, allow_nan=False))
