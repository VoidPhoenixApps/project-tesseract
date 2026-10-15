"""D6 deterministic desk model; synthetic inputs, no hardware or G-code interface."""
from dataclasses import dataclass, field
import json
import math

MODES = {
    'S': ((1,), (2,), (3,), (4,)), 'R': ((1, 2), (3, 4)),
    'C': ((1, 3), (2, 4)), 'M12': ((1, 2), (3,), (4,)),
    'M34': ((3, 4), (1,), (2,)), 'M13': ((1, 3), (2,), (4,)),
    'M24': ((2, 4), (1,), (3,)), 'J': ((1, 2, 3, 4),),
}


def nonnegative(*values):
    if any(isinstance(v, bool) or not math.isfinite(v) or v < 0 for v in values):
        raise ValueError('expected finite nonnegative numbers')


@dataclass(frozen=True)
class Box:
    """Closed AABB in mm; touching counts as conflict. Includes input margin."""
    lo: tuple
    hi: tuple

    def __post_init__(self):
        if len(self.lo) != 3 or len(self.hi) != 3:
            raise ValueError('3D bounds required')
        if any(not math.isfinite(x) for x in self.lo + self.hi):
            raise ValueError('nonfinite geometry')
        if any(a >= b for a, b in zip(self.lo, self.hi)):
            raise ValueError('positive extent required')

    def intersects(self, other):
        return all(a <= d and c <= b for a, b, c, d in
                   zip(self.lo, self.hi, other.lo, other.hi))

    def contains(self, other):
        return all(a <= c and d <= b for a, b, c, d in
                   zip(self.lo, self.hi, other.lo, other.hi))


@dataclass(frozen=True)
class Job:
    name: str
    beds: tuple
    head: int
    objects: tuple  # union of conservative object volumes, including support/brim
    sweeps: tuple   # union of conservative whole-motion envelopes for entire job
    reach: Box     # assumed whole-assembly allowed envelope, not nominal bed size
    resources: frozenset
    watts: float   # concurrent worst-case DC allocation, not mean heater duty
    speed: float   # hypothetical progress mm/s, not nozzle feedrate
    height: float
    bed_c: float = 60
    nozzle_c: float = 210
    layer_mm: float = 0.2

    def __post_init__(self):
        nonnegative(self.watts, self.speed, self.height, self.bed_c, self.nozzle_c,
                    self.layer_mm)
        if (not self.name or self.head not in range(1, 5) or not self.objects
                or not self.sweeps or self.height == 0 or self.layer_mm == 0):
            raise ValueError('incomplete job')
        if self.beds != tuple(sorted(set(self.beds))) or not set(self.beds) <= {1, 2, 3, 4}:
            raise ValueError('invalid bed group')

    @property
    def claims(self):
        return self.resources | frozenset(['head:%s' % self.head] +
                                         ['bed:%s' % b for b in self.beds])


@dataclass
class Run:
    job: Job
    state: str = 'RUNNING'
    progress: float = 0.0


@dataclass
class Evidence:
    """Injected synthetic evidence only, never physical proof."""
    stamp: float = 0.0
    healthy: bool = True
    connected: bool = True
    position_known: bool = True
    sheets_ready: bool = True
    locks_confirmed: bool = True
    guard_permitted: bool = True
    thermal_ready: bool = True
    at_datum: bool = True

    def usable(self, now, ttl):
        return (0 <= now - self.stamp <= ttl and self.healthy and self.connected
                and self.position_known and self.sheets_ready and self.locks_confirmed
                and self.guard_permitted and self.thermal_ready)


@dataclass
class Model:
    mode: str = 'S'
    budget: float = 1200
    ttl: float = 1.0
    evidence: Evidence = field(default_factory=Evidence)
    state: str = 'READY'
    now: float = 0.0
    runs: dict = field(default_factory=dict)
    parks: dict = field(default_factory=dict)  # head -> (complete park volume, reachable)
    obstacles: tuple = ()
    history: list = field(default_factory=list)

    def __post_init__(self):
        if self.mode not in MODES:
            raise ValueError('unknown mode')
        nonnegative(self.budget, self.ttl)

    def fault(self, reason):
        self.state = 'FAULT_LATCHED'
        self.history.append(('fault', reason))
        for run in self.runs.values():
            if run.state in ('RUNNING', 'PAUSED'):
                run.state = 'FAULTED'
        # Occupancy and all reservations deliberately retained.

    def check(self):
        if self.state == 'FAULT_LATCHED':
            return False
        if not self.evidence.usable(self.now, self.ttl):
            self.fault('missing/stale/failed evidence or disconnected controller')
            return False
        return self.state == 'READY'

    def admit(self, jobs):
        """Atomic batch admission. Failure obtains no resources; no hold-and-wait."""
        if not self.check():
            return False, 'inhibited'
        jobs = tuple(jobs)
        if not jobs or len({j.name for j in jobs}) != len(jobs):
            return False, 'duplicate/empty batch'
        old = [r.job for r in self.runs.values()]
        all_jobs = old + list(jobs)
        if any(j.name in self.runs or j.beds not in MODES[self.mode] for j in jobs):
            return False, 'identity/group'
        claimed = set()
        for j in all_jobs:
            if claimed & j.claims:
                return False, 'resource conflict'
            claimed.update(j.claims)
        if sum(j.watts for j in all_jobs) > self.budget:
            return False, 'power budget'
        active_heads = {j.head for j in all_jobs}
        park_boxes = []
        for h in set(range(1, 5)) - active_heads:
            if h not in self.parks or not self.parks[h][1]:
                return False, 'unreachable/unknown park'
            park_boxes.append(self.parks[h][0])
        for i, park in enumerate(park_boxes):
            if any(park.intersects(b) for b in park_boxes[i + 1:] + list(self.obstacles)):
                return False, 'occupied park'
        for i, j in enumerate(all_jobs):
            if any(not j.reach.contains(b) for b in j.sweeps + j.objects):
                return False, 'unreachable geometry'
            blocks = list(self.obstacles) + park_boxes
            for other in all_jobs[i + 1:]:
                if any(a.intersects(b) for a in j.sweeps + j.objects
                       for b in other.sweeps + other.objects):
                    return False, 'job geometry conflict'
            if any(a.intersects(b) for a in j.sweeps + j.objects for b in blocks):
                return False, 'obstacle/park collision'
        for j in jobs:
            self.runs[j.name] = Run(j)
        self.history.append(('admit', [j.name for j in jobs]))
        return True, 'synthetic admission only'

    def advance(self, seconds):
        nonnegative(seconds)
        self.now += seconds
        if not self.check():
            return
        for run in self.runs.values():
            if run.state == 'RUNNING':
                run.progress = min(run.job.height, run.progress + run.job.speed * seconds)
                if run.progress == run.job.height:
                    run.state = 'FINISHED_OCCUPIED'

    def pause(self, name):
        if not self.check() or self.runs[name].state != 'RUNNING':
            return False
        self.runs[name].state = 'PAUSED'
        return True

    def resume(self, name):
        if not self.check() or self.runs[name].state != 'PAUSED':
            return False
        self.runs[name].state = 'RUNNING'
        return True

    def cancel(self, name):
        if not self.check() or self.runs[name].state not in ('RUNNING', 'PAUSED'):
            return False
        self.runs[name].state = 'CANCELLED_OCCUPIED'
        return True

    def clear(self, name, *, removal_confirmed=False, cool=False, isolated_access=False):
        # Synthetic supervised removal; no real access authorization.
        if self.runs[name].state not in ('FINISHED_OCCUPIED', 'CANCELLED_OCCUPIED', 'FAULTED'):
            return False
        if not (removal_confirmed and cool and isolated_access):
            return False
        del self.runs[name]
        return True

    def transition(self, target, affected, route, *, support_proven=False):
        """Atomic abstract transition, NOT an executable docking sequence."""
        if not self.check():
            return False, 'inhibited'
        if target not in MODES or not route or not support_proven or not self.evidence.at_datum:
            return False, 'missing transition evidence'
        changed = set()
        for b in range(1, 5):
            old = next(g for g in MODES[self.mode] if b in g)
            new = next(g for g in MODES[target] if b in g)
            if old != new:
                changed.add(b)
        if not changed <= set(affected) or not set(affected) <= {1, 2, 3, 4}:
            return False, 'incomplete affected domain'
        for run in self.runs.values():
            if set(run.job.beds) & set(affected):
                return False, 'occupied affected bed'
        blocks = list(self.obstacles)
        blocks += [b for run in self.runs.values() for b in run.job.objects + run.job.sweeps]
        # All otherwise idle heads must have established parks before conversion.
        for h in set(range(1, 5)) - {r.job.head for r in self.runs.values()}:
            if h not in self.parks or not self.parks[h][1]:
                return False, 'unknown transition park'
            park = self.parks[h][0]
            if any(park.intersects(b) for b in blocks):
                return False, 'occupied transition park'
            blocks.append(park)
        if any(a.intersects(b) for a in route for b in blocks):
            return False, 'transition collision'
        self.history.append(('transition', self.mode, target))
        self.mode = target
        return True, 'abstract transition only'

    def reset(self, *, human_ack=False):
        if self.state != 'FAULT_LATCHED' or not human_ack:
            return False
        if self.runs or not self.evidence.usable(self.now, self.ttl):
            return False
        self.state = 'READY'  # No queued command or job is restarted.
        self.history.append(('reset', 'manual synthetic acknowledgement'))
        return True


def power(bed_w=120, nozzle_w=60, bed_duty=0.35, nozzle_duty=0.3,
          motion_w=120, auxiliary_w=40, accessory_w=0, voltage=24, efficiency=0.9):
    nonnegative(bed_w, nozzle_w, motion_w, auxiliary_w, accessory_w, voltage,
                efficiency, bed_duty, nozzle_duty)
    if not (0 < efficiency <= 1 and voltage > 0 and bed_duty <= 1 and nozzle_duty <= 1):
        raise ValueError('invalid duty/efficiency/voltage')
    base = motion_w + auxiliary_w + accessory_w
    peak = 4 * bed_w + 4 * nozzle_w + base
    typical = 4 * bed_w * bed_duty + 4 * nozzle_w * nozzle_duty + base
    return dict(peak_dc_w=peak, typical_dc_w=typical, peak_dc_a=peak / voltage,
                peak_ac_real_w=peak / efficiency,
                one_bed_start_dc_w=bed_w + 3 * bed_w * bed_duty + 4 * nozzle_w + base)


def demo():
    return {'evidence': 'hypothetical arithmetic, not hardware predictions',
            'modes': MODES,
            'power_cases': {str(w): power(bed_w=w) for w in (80, 120, 180)},
            'latency_distance_mm': {str(t): 100 * t for t in (0.005, 0.025, 0.1)}}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2, sort_keys=True))
