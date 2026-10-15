"""D5 research sensitivities; SI except explicitly named mm. No hardware model.
Python 3.9+ standard library. See d5-calculations.md for assumptions/limits.
"""
import json
from math import exp, isfinite
from dataclasses import replace
from d2_geometry import Box, MODES, Parameters, mode_screen, path_hits
from d4_analysis import positive, nonnegative

# Reference properties, not allowable design values; d5-references M1/M2/M5/M6.
MATERIALS = {
    'pc_reference': (1200, 65e-6, 2.3e9, .21),
    'pmma_reference': (1190, 70e-6, 3.3e9, .19),
    'glass_property_proxy': (2500, 9e-6, 70e9, 1.0),
    'al5754_reference': (2660, 23.9e-6, 70.5e9, 150),
}


def growth(length, alpha, delta_t):
    positive(length)
    nonnegative(alpha)
    if not isfinite(delta_t):
        raise ValueError('finite temperature difference required')
    return length*alpha*delta_t


def panel_mass(width, height, thickness, density):
    positive(width, height, thickness, density)
    return width*height*thickness*density


def strip_deflection(pressure, span, thickness, modulus):
    """Simply supported unit-width strip, uniform pressure; not a 2-D plate."""
    nonnegative(pressure)
    positive(span, thickness, modulus)
    w = 5*pressure*span**4/(32*modulus*thickness**3)
    return {'deflection_mm': 1000*w, 'w_over_t': w/thickness,
            'linear_warning': w/thickness >= .5}


def retention(mass, acceleration, outward_force, eccentricity, spacing, supports):
    """Ideal lower supports share vertical load; upper retainers resist moment.
    Outward force applied at mid-height; all dimensions m. No impact/capacity.
    """
    positive(mass, spacing)
    nonnegative(acceleration, outward_force, eccentricity)
    if type(supports) is not int or supports < 1:
        raise ValueError('positive integer support count required')
    weight = mass*(9.81+acceleration)
    moment = weight*eccentricity + outward_force*spacing/2
    return {'vertical_total_n': weight, 'ideal_per_support_n': weight/supports,
            'upper_retainer_total_n': moment/spacing,
            'lower_normal_reaction_n': outward_force-moment/spacing}


def heat_conductance(area, thickness, conductivity, h_inside, h_outside,
                     leakage_m3_h, bridge_w_k=0):
    positive(area, thickness, conductivity, h_inside, h_outside)
    nonnegative(leakage_m3_h, bridge_w_k)
    u = 1/(1/h_inside+thickness/conductivity+1/h_outside)
    # Constant representative air density/cp, sensitivity only.
    return area*u + 1.2*1005*leakage_m3_h/3600 + bridge_w_k


def lumped_rise(power, conductance, capacity, seconds, initial_rise=0):
    nonnegative(power, seconds, initial_rise)
    positive(conductance, capacity)
    steady = power/conductance
    tau = capacity/conductance
    return {'steady_rise_k': steady, 'tau_s': tau,
            'rise_k': steady+(initial_rise-steady)*exp(-seconds/tau)}


def two_zone(q_lower, q_upper, g_lower, g_upper, mixing):
    """Two steady temperature rises; positive losses to common ambient."""
    nonnegative(q_lower, q_upper, mixing)
    positive(g_lower, g_upper)
    det = g_lower*g_upper+mixing*(g_lower+g_upper)
    low = (q_lower*(g_upper+mixing)+mixing*q_upper)/det
    high = (q_upper*(g_lower+mixing)+mixing*q_lower)/det
    return {'lower_rise_k': low, 'upper_rise_k': high,
            'difference_k': high-low,
            'loss_w': g_lower*low+g_upper*high}


def friction_reserve(preload, remaining_fraction, friction, shear):
    nonnegative(preload, remaining_fraction, friction, shear)
    if remaining_fraction > 1:
        raise ValueError('remaining fraction exceeds one')
    capacity = preload*remaining_fraction*friction
    return {'assumed_friction_n': capacity, 'reserve_n': capacity-shear}


def removal_example():
    # Abstract panel and overhead lip, mm. Not vendor or proposed CAD geometry.
    panel = Box((-300, 320, 0), (300, 324, 600))
    lip = Box((-310, 310, 615), (310, 350, 630))
    lift_then_out = [(0,0,0), (0,0,40), (0,100,40)]
    out_then_lift = [(0,0,0), (0,100,0), (0,100,40)]
    return {'installed_overlap': panel.overlaps(lip),
            'lift_then_out_hit_segments': path_hits(panel,lift_then_out,lip),
            'out_then_lift_hit_segments': path_hits(panel,out_then_lift,lip),
            'reverse_install_hit_segments': path_hits(panel,list(reversed(out_then_lift)),lip),
            'limits': 'Translation only; alternate order requires an interface that permits it. Hands, rotation and other obstacles absent.'}


def results():
    panels = {}
    for name, (rho, alpha, modulus, conductivity) in MATERIALS.items():
        thickness = .0015 if name == 'al5754_reference' else .004
        panels[name] = {
            'thickness_m': thickness,
            'mass_kg': panel_mass(.6,.6,thickness,rho),
            'growth_mm_at_40k': 1000*growth(.6,alpha,40),
            'relative_to_steel_mm_panel40k_frame20k': 1000*(growth(.6,alpha,40)-growth(.6,12e-6,20)),
            'strip_at_50pa': strip_deflection(50,.6,thickness,modulus),
            'conductance_w_k_at_5m3h': heat_conductance(2.16,thickness,conductivity,4,8,5),
        }
    thermal = []
    for power in (100,300,600):
        for flow in (0,5,20):
            g = heat_conductance(2.16,.004,.21,4,8,flow)
            thermal.append({'power_w':power,'leakage_m3_h':flow,'g_w_k':g,
                            **lumped_rise(power,g,10000,1800)})
    clearances = []
    for topology in ('moving-bridge','stacked-bridge'):
        for inner in (300,320,360):
            for mode in MODES:
                r = mode_screen(mode,replace(Parameters(),frame_inner=inner+20),topology)
                clearances.append({'mode':mode,'topology':topology,'clear_half_width_mm':inner,
                    'outside':r['enclosure_outside'], 'inherited_status':r['classification'],
                    'panels_removed_status':'UNRESOLVED: same internal collision and reach obligations; guards absent from model'})
    return {'status':'Hypothetical research; no physical validation or capacity rating',
            'panels':panels,'thermal':thermal,
            'thermal_two_zone':[{'mixing_w_k':m,**two_zone(80,220,4,4,m)} for m in (1,4,20)],
            'retention_glass':[{'supports':n,**retention(3.6,2,30,.03,.5,n)} for n in (2,1)],
            'creep_sensitivity':[{'remaining_fraction':f,**friction_reserve(200,f,.2,20)} for f in (1,.5,.25)],
            'frame_growth_mm':{'steel_20k':1000*growth(.6,12e-6,20),
                'al_20k':1000*growth(.6,23.6e-6,20),'steel_5k_gradient':1000*growth(.6,12e-6,5)},
            'removal':removal_example(), 'clearance_sensitivity':clearances}


if __name__ == '__main__':
    print(json.dumps(results(), indent=2, sort_keys=True, allow_nan=False))
