"""D9 abstract obligation checks, NOT a controller or a mechanical safety solver.

Paths and assertions are supplied assumptions. No capacity, contact or 6-DOF solve.
Python 3.9+ standard library; deterministic JSON on stdout.
"""
from dataclasses import dataclass
import json
from math import isfinite

from d2_geometry import MODES
from d3_analysis import G, arrest, cantilever, guide_loop, reactions


@dataclass(frozen=True)
class Observation:
    epoch: int
    time_s: float
    downstream: bool
    agrees: bool

    def usable(self, epoch, now_s, max_age_s):
        """Illustrative policy bounds supplied by caller, never physical limits."""
        values = (self.time_s, now_s, max_age_s)
        return (all(isfinite(x) for x in values) and max_age_s >= 0
                and self.epoch == epoch and self.downstream and self.agrees
                and 0 <= now_s-self.time_s <= max_age_s)


def affected_beds(before, after, influence=()):
    """Membership changes plus transitive undirected support/reference influence.

    Caller must supply ALL influence edges; omission can falsely isolate a neighbor.
    No geometric trajectory or compliant-frame isolation is inferred.
    """
    a = {i: frozenset(g) for g in MODES[before] for i in g}
    b = {i: frozenset(g) for g in MODES[after] for i in g}
    affected = {i for i in a if a[i] != b[i]}
    if any(x not in a or y not in a for x, y in influence):
        raise ValueError('influence endpoints must be bed IDs')
    while True:
        expanded = affected | {v for edge in influence if affected.intersection(edge) for v in edge}
        if expanded == affected:
            return affected
        affected = expanded


def surviving_path(paths, failed):
    """Nonempty named paths; capacity/anchor independence NOT inferred from names."""
    return any(path and not set(path).intersection(failed) for path in paths)


def uncovered(inventory, support, restraint, failed=()):
    """Report missing L and R paths for every named gravity-loaded body, idle too."""
    return {body: [kind for kind, graph in (('L', support), ('R', restraint))
                   if not surviving_path(graph.get(body, ()), failed)]
            for body in inventory
            if (not surviving_path(support.get(body, ()), failed)
                or not surviving_path(restraint.get(body, ()), failed))}


@dataclass(frozen=True)
class Transfer:
    old_support: bool
    new_support: bool
    restraint: bool
    compatible: bool
    load_accepted: bool
    observed: bool
    at_datum: bool = True
    selector_full: bool = True
    torque_enabled: bool = False


def transfer_errors(states, occupied=(), affected=()):
    """Discrete contract checker only; continuous trajectories are not certified.

    Booleans mean externally established evidence in the hypothetical model, not
    command/switch values. Load acceptance and compatibility have no real proof yet.
    """
    errors = []
    if set(occupied).intersection(affected):
        errors.append('occupied affected bed')
    if not states:
        return errors + ['empty sequence']
    for i, state in enumerate(states):
        if not (state.old_support or state.new_support):
            errors.append(f'{i}: unsupported')
        if not state.restraint:
            errors.append(f'{i}: missing restraint')
        if not state.compatible:
            errors.append(f'{i}: incompatible constraints')
        if not state.observed:
            errors.append(f'{i}: unknown observation')
        if not state.at_datum:
            errors.append(f'{i}: off reconfiguration datum')
        if state.torque_enabled and not state.selector_full:
            errors.append(f'{i}: torque through partial selector')
        if not state.old_support and not (state.new_support and state.load_accepted):
            errors.append(f'{i}: unproven receiving support')
        if i and states[i-1].old_support and not state.old_support:
            previous = states[i-1]
            if not (previous.new_support and previous.load_accepted and previous.observed
                    and previous.restraint and previous.compatible):
                errors.append(f'{i}: release before verified overlap')
    return errors


def handoff():
    return [Transfer(True, False, True, True, False, True),
            Transfer(True, True, True, True, False, True),
            Transfer(True, True, True, True, True, True),
            Transfer(False, True, True, True, True, True)]


def results():
    inventory = [f'bed{i}' for i in range(1, 5)] + [f'head{i}' for i in range(1, 5)] + ['unused_platform']
    # Deliberately synthetic dependency names: NOT a constructed machine graph.
    support = {b: [(b+'-support', 'shared-root')] for b in inventory}
    restraint = {b: [(b+'-catch', 'shared-root')] for b in inventory}
    transitions = [('S', 'M12'), ('M12', 'R'), ('R', 'C'), ('M24', 'J')]
    return {
        'status': 'Abstract counterexamples and illustrative sensitivities; no physical validation',
        'owners': {m: [list(g) for g in groups] for m, groups in MODES.items()},
        'affected_without_extra_influence': {a+'->'+b: sorted(affected_beds(a, b)) for a, b in transitions},
        'S_to_M12_with_shared_2_3_reference': sorted(affected_beds('S', 'M12', ((2, 3),))),
        'shared_root_failure_uncovered': uncovered(inventory, support, restraint, ('shared-root',)),
        'handoff_contract_errors': transfer_errors(handoff()),
        'release_without_overlap_errors': transfer_errors([handoff()[0], handoff()[-1]]),
        'reaction_sweep': [dict(e_mm=e, force_n=12*G, spacing_mm=240,
                                reactions_n=reactions(12*G, 240, e)) for e in (-150, -120, 0, 120, 150)],
        'arm_sweep': [dict(force_n=20, length_mm=l, ei_n_mm2=1e7,
                           **cantilever(20, l, 1e7)) for l in (90, 180, 360)],
        'guide_sweep': [dict(travel_mm=h, angle_deg=.05, initial_mm=.02,
                             free_mm=.05, stiffness_n_mm=1000,
                             **guide_loop(h, .05, .02, .05, 1000)) for h in (0, 100, 200)],
        'arrest_sweep': [dict(mass_kg=m, delay_s=t, downward_speed_m_s=.01,
                              stopping_stroke_mm=1, **arrest(m, .01, t, 1))
                         for m in (1, 4, 12) for t in (.01, .02, .05)],
    }


if __name__ == '__main__':
    print(json.dumps(results(), indent=2, sort_keys=True))
