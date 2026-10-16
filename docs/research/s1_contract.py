"""S1 synthetic metadata/epoch admission wrapper around D6. No firmware or I/O."""
from dataclasses import dataclass, replace
import json
from d6_model import Box, Job, Model, MODES


@dataclass(frozen=True)
class Submission:
    job: Job
    epochs: tuple  # (bed, generation); synthetic observations, not sensor evidence
    profile: str
    mesh: str
    dialect: str
    bed_targets: tuple


class Coordinator:
    """Single-threaded desk contract, NOT a production controller or G-code parser."""
    def __init__(self, mode='S'):
        parks = {h: (Box((h * 30, -100, 0), (h * 30 + 10, -90, 10)), True)
                 for h in range(1, 5)}
        self.model = Model(mode=mode, budget=2000, ttl=100, parks=parks)
        self.epochs = {b: 0 for b in range(1, 5)}

    def stamp(self, job, dialect='klipper'):
        return Submission(job, tuple((b, self.epochs[b]) for b in job.beds),
                          'synthetic-profile-1', 'synthetic-mesh-1', dialect,
                          tuple((b, job.bed_c) for b in job.beds))

    def admit(self, submissions):
        submissions = tuple(submissions)
        for s in submissions:
            if s.epochs != tuple((b, self.epochs[b]) for b in s.job.beds):
                return False, 'stale configuration'
            if not s.profile or not s.mesh or s.dialect not in ('klipper', 'rrf'):
                return False, 'unsupported metadata'
            # Deliberately narrow coherent recipe; differential calibration unmodeled.
            if s.bed_targets != tuple((b, s.job.bed_c) for b in s.job.beds):
                return False, 'incoherent group temperature'
        return self.model.admit(s.job for s in submissions)

    def transition(self, target, affected, route, *, support_proven=False):
        affected = tuple(affected)
        result = self.model.transition(target, affected, route,
                                       support_proven=support_proven)
        if result[0]:
            for b in set(affected):
                self.epochs[b] += 1
        return result

    def reset(self, *, human_ack=False):
        result = self.model.reset(human_ack=human_ack)
        if result:
            for b in self.epochs:
                self.epochs[b] += 1
        return result

    def fault(self, reason):
        # Conservative global scope; no inferred independent physical fault domains.
        self.model.fault(reason)
        for b in self.epochs:
            self.epochs[b] += 1


def synthetic_jobs(mode='S'):
    """Disjoint strips; not bed geometry, actual toolpaths or validated envelopes."""
    return [Job('j%d' % i, group, i,
                (Box((i * 100, 0, 0), (i * 100 + 10, 10, 20)),),
                (Box((i * 100 - 5, -5, -5), (i * 100 + 15, 15, 30)),),
                Box((-1000, -1000, -1000), (1000, 1000, 1000)),
                frozenset(['z:%d' % b for b in group] +
                          ['heater:%d' % b for b in group]),
                200, i, 20 * i, 50 + 5 * i, 190 + 10 * i, .1 * i)
            for i, group in enumerate(MODES[mode], 1)]


def demo():
    c = Coordinator()
    jobs = synthetic_jobs()
    jobs[0] = replace(jobs[0], height=2)
    events = []

    def snapshot(label):
        events.append({'event': label, 'runs': {
            name: {'state': r.state, 'progress_mm': r.progress}
            for name, r in c.model.runs.items()}})

    events.append({'admit_first': c.admit([c.stamp(jobs[0])])})
    c.model.advance(1)
    events.append({'late_arrivals': c.admit([c.stamp(j) for j in jobs[1:]])})
    c.model.advance(.5)
    snapshot('four running independently')
    c.model.pause('j2')
    c.model.cancel('j3')
    c.model.advance(.5)
    snapshot('finish one, pause one, cancel one, fourth progresses')
    route = (Box((-20, 0, 0), (-10, 10, 10)),)
    events.append({'occupied_conversion': c.transition('M12', (1, 2), route,
                                                       support_proven=True)})
    c.fault('synthetic lost executor')
    snapshot('global fault retains objects and reservations')
    return {'evidence': 'synthetic contract only; no G-code or firmware executed',
            'events': events}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2, sort_keys=True))
