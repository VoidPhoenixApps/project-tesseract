"""D8 hypothetical box mechanisms, mm. No vendor geometry or feasibility pass.
Reuse D2 continuous rigid-box collision, orientation and eight final layouts.
Run with --write to reproduce JSON and readable mode/sensitivity summary.
"""
from dataclasses import dataclass, asdict, replace
from itertools import combinations, product
from pathlib import Path
import argparse
import json
import math
from d2_geometry import Box, Parameters, MODES, ASSIGNMENTS, regions, oriented, ccd, hull


@dataclass(frozen=True)
class Envelope:
    root: float = 320
    rail: float = 600
    engagement: float = 30
    tangential: float = 300
    park: float = 260
    body_scale: float = 1
    cable: float = 30
    halfwidth: float = 520
    roof: float = 700
    reserve: float = 2
    head_stroke: float = 240
    bed_stroke: float = 240
    arm_width: float = 30
    finished_height: float = 200

    def __post_init__(self):
        if any(not math.isfinite(v) or v <= 0 for v in asdict(self).values()):
            raise ValueError('positive finite hypothetical dimensions required')
        if self.rail <= 2*self.engagement:
            raise ValueError('rail must retain two engagement margins')


SIGNS = {1: (-1, 1), 2: (1, 1), 3: (-1, -1), 4: (1, -1)}


def level(head):
    return 420 + (head-1)*40


def functional_parts(head, p, mirror):
    """Separate functional allocations, not manufactured mirrored vendor solids."""
    s = p.body_scale
    boxes = {
        'nozzle': Box((-2,-2,0),(2,2,5)),
        'heater-hotend': Box((-8,-8,5),(8,8,35)),
        'fan-duct': Box((-50*s,-8*s,10),(8*s,50*s,70)),
        'motor': Box((-45,-5,65),(-5,35,100)),
        'probe-deployed-reserve': Box((-25,-10,2),(-15,0,35)),
        'head-carriage': Box((-40,5,35),(0,35,65)),
        'cable-local': Box((-50-p.cable,15,30),(-40,35,120)),
        'filament-local': Box((-50-p.cable,20,85),(-20,40,150)),
    }
    return {n: oriented(b,head,mirror) for n,b in boxes.items()}


def assembly(head, xyz, architecture, p, mirror=True):
    """Named world boxes. Every bound is affine along each supplied segment.
    Full-length radial rail translates past a fixed X root; it does NOT telescope.
    Head-Z rail has fixed length, travels with nozzle, protrudes above XY level.
    Root return cable is a conservative variable-length rectangular reservation.
    """
    if architecture not in ('H','B'):
        raise ValueError('R transformation has no geometric certificate')
    x,y,z=xyz; sx,_=SIGNS[head]; root=sx*p.root; lev=level(head)
    out={n:b.move(xyz) for n,b in functional_parts(head,p,mirror).items()}
    w=p.arm_width/2
    ends=(x,x+sx*p.rail)
    out['moving-radial-rail']=Box((min(ends),y-w,lev),(max(ends),y+w,lev+30))
    out['root-carriage-motor']=Box((root-25,y-30,lev-15),(root+25,y+30,lev+55))
    out['fixed-tangential-guide']=Box((root-15,-p.tangential-30,lev),
                                      (root+15,p.tangential+30,lev+30))
    # Symmetric column avoids granting E a free structural redesign.
    top=z+lev+30 if architecture=='H' else lev+30
    out['Z-column']=Box((x-15,y-15,z+35),(x+15,y+15,top))
    out['root-cable-reservation']=Box((min(x,root)-p.cable,y-20,lev+35),
                                       (max(x,root)+p.cable,y+20,lev+65))
    return out


def affine_contact(a0,a1,b0,b1,reserve=0):
    """Exact interval for linearly varying AABB bounds; touching is interference.
    Rigid special case delegates to D2. Affine boxes are still only envelopes.
    """
    if not math.isfinite(reserve) or reserve < 0:
        raise ValueError('nonnegative finite reservation required')
    # Conservative union disjointness cheaply rejects impossible intervals.
    # Affine bounds reach extrema at endpoints; reserve expands A only.
    for i in range(3):
        if (min(a0.lo[i],a1.lo[i])-reserve > max(b0.hi[i],b1.hi[i])
                or min(b0.lo[i],b1.lo[i]) > max(a0.hi[i],a1.hi[i])+reserve):
            return None
    a0=a0.inflate(reserve); a1=a1.inflate(reserve)
    da=tuple(a1.lo[i]-a0.lo[i] for i in range(3))
    db=tuple(b1.lo[i]-b0.lo[i] for i in range(3))
    if all(a1.hi[i]-a0.hi[i]==da[i] and b1.hi[i]-b0.hi[i]==db[i] for i in range(3)):
        return ccd(a0,(0,0,0),da,b0,(0,0,0),db)
    enter,leave=0.,1.
    for i in range(3):
        for q0,q1 in ((a0.lo[i]-b0.hi[i],a1.lo[i]-b1.hi[i]),
                      (b0.lo[i]-a0.hi[i],b1.lo[i]-a1.hi[i])):
            slope=q1-q0
            if slope==0:
                if q0>0: return None
            elif slope>0: leave=min(leave,-q0/slope)
            else: enter=max(enter,-q0/slope)
            if enter>leave: return None
    return (enter,leave)


def park(head,z,p):
    sx,sy=SIGNS[head]
    return (sx*p.park,sy*p.park,z)


def route(region,head,z,p,kind):
    """Six vertices. Printing witnesses include corners, a diagonal and center.
    Departure goes outward X then Y; approach is exactly its reverse, no teleport.
    """
    x0,y0=region.lo[:2]; x1,y1=region.hi[:2]
    sx,sy=SIGNS[head]; home=(x0 if sx<0 else x1,y1 if sy>0 else y0,z)
    center=((x0+x1)/2,(y0+y1)/2,z)
    if kind=='print':
        return [(x0,y0,z),(x1,y0,z),(x1,y1,z),(x0,y1,z),(x1,y0,z),center]
    points=[center,home,(sx*p.park,home[1],z),park(head,z,p),park(head,z,p),park(head,z,p)]
    return list(reversed(points)) if kind=='approach' else points


def reach(head,points,architecture,p):
    sx,_=SIGNS[head]
    return all(p.engagement <= p.root-sx*x <= p.rail-p.engagement
               and abs(y)<=p.tangential and 0<=z<=(p.head_stroke if architecture=='H' else 0)
               for x,y,z in points)


def scene(mode,architecture,mirror,p,panels,kind='print',finished=None,moving_owner=None):
    rs=regions(mode,Parameters()); owners=ASSIGNMENTS[mode]
    heights=(10,150,60,200)[:len(owners)]
    paths={}; objects={}; bed_depths=[]
    for j,(head,r,height) in enumerate(zip(owners,rs,heights)):
        height=p.finished_height if head==finished else height
        depth=height if architecture=='B' else 0
        bed_depths.append(depth)
        objects[head]=Box((r.lo[0],r.lo[1],-depth),(r.hi[0],r.hi[1],height-depth))
        z=height if architecture=='H' else 0
        paths[head]=[park(head,z,p)]*6 if head==finished else route(r,head,z,p,kind if moving_owner in (None,head) else 'print')
    for head in set(range(1,5))-set(owners):
        paths[head]=[park(head,200 if architecture=='H' else 0,p)]*6
    samples={head:[assembly(head,q,architecture,p,mirror) for q in path] for head,path in paths.items()}
    counts={'object':0,'assembly':0,'boundary':0,'self':0}
    witnesses={}
    def record(category,label,segment,interval=None):
        counts[category]+=1
        witnesses.setdefault(category,{'pair':label,'segment':segment,'interval':interval})
    # Endpoints suffice for containment of affine bounds in a convex box.
    inner=p.halfwidth-(20 if panels else 0)
    room=Box((-inner,-inner,-300),(inner,inner,p.roof if panels else 10000))
    for head,poses in samples.items():
        for i,pose in enumerate(poses):
            for name,b in pose.items():
                if not room.contains(b.inflate(p.reserve)): record('boundary',f'H{head}:{name}',i)
        for i,(a,b) in enumerate(zip(poses,poses[1:])):
            for name in a:
                for owner,obj in objects.items():
                    if owner==head and head!=finished and name=='nozzle': continue
                    # Own ideal object ends at deposition plane. Reserve is not
                    # applied to intentional own workpiece adjacency.
                    c=0 if owner==head else p.reserve
                    interval=affine_contact(a[name],b[name],obj,obj,c)
                    if interval is not None: record('object',f'H{head}:{name}/object-H{owner}',i,interval)
            # Noncontacting self parts only. Mount/guide intended interfaces excluded.
            for name in ('fan-duct','motor','cable-local','filament-local'):
                interval=affine_contact(a[name],b[name],a['moving-radial-rail'],b['moving-radial-rail'],p.reserve)
                if interval is not None: record('self',f'H{head}:{name}/own-rail',i,interval)
    for h,k in combinations(range(1,5),2):
        for i in range(5):
            for n,m in product(samples[h][i],samples[k][i]):
                interval=affine_contact(samples[h][i][n],samples[h][i+1][n],
                                        samples[k][i][m],samples[k][i+1][m],p.reserve)
                if interval is not None: record('assembly',f'H{h}:{n}/H{k}:{m}',i,interval)
    # Independent timing: spatial hull intersection is ONLY a reservation candidate.
    hull_candidates=0
    for h,k in combinations(range(1,5),2):
        for n,m in product(samples[h][0],samples[k][0]):
            if hull(q[n] for q in samples[h]).inflate(p.reserve).overlaps(hull(q[m] for q in samples[k])):
                hull_candidates+=1
    failed=[h for h in paths if not reach(h,paths[h],architecture,p)]
    return {'mode':mode,'architecture':architecture,'orientation':'E' if mirror else 'common',
            'panels':'enclosed' if panels else 'open','route':kind,'finished_owner':finished,'moving_owner':moving_owner,
            'failed_head_strokes':failed,'bed_stroke_failed':max(bed_depths)>p.bed_stroke,
            'events':counts,'first_witnesses':witnesses,'independent_hull_candidates':hull_candidates,
            'status':'UNRESOLVED_REAL_MACHINE'}


def witnesses():
    body=Box((-5,-5,10),(5,5,70)); obstacle=Box((-10,-10,0),(10,10,200))
    return {
        'midpath_tall_object': {'interval':ccd(body,(-30,0,10),(30,0,10),obstacle),
                              'endpoint_hits':[body.move(q).overlaps(obstacle) for q in [(-30,0,10),(30,0,10)]]},
        'bed_down_200_vs_stationary': {
            'H_interval':ccd(body,(-30,0,10),(30,0,10),obstacle),
            'B_interval':ccd(body,(-30,0,0),(30,0,0),obstacle.move((0,0,-200)))},
        'park_blocked_rail': {'interval':ccd(Box((-600,-15,420),(0,15,450)),
            (-175,200,0),(-260,260,0),Box((-800,240,410),(-700,280,460)))},
        'head_Z_column_rise': {'interval':affine_contact(
            assembly(1,(0,0,0),'H',Envelope())['Z-column'],
            assembly(1,(0,0,200),'H',Envelope())['Z-column'],
            Box((-20,-20,470),(20,20,500)),Box((-20,-20,470),(20,20,500)))},
        'bed_lowering_understructure': {'interval':ccd(Box((-20,-20,-30),(20,20,-5)),
            (0,0,0),(0,0,-200),Box((-30,-30,-110),(30,30,-100)))},
        'adjacent_live_jobs': {'interval':ccd(body,(-30,0,10),(30,0,10),body,(30,0,10),(-30,0,10))},
        'nonpassing_bridge_order': 'y1+w+c < y2 excludes arbitrary column trajectories; bypass changes topology',
    }


def results():
    p=Envelope()
    baseline=[scene(m,a,e,p,panels,kind,finished)
        for m,a,e,panels in product(MODES,('H','B'),(False,True),(False,True))
        for kind,finished in [('print',None),('departure',None),('approach',None)]+[('print',h) for h in ASSIGNMENTS[m]]]
    baseline += [scene(m,a,e,p,panels,kind,moving_owner=head)
        for m,a,e,panels in product(MODES,('H','B'),(False,True),(False,True))
        for head,kind in product(ASSIGNMENTS[m],('departure','approach'))]
    # OFAT studies; not a claim that the Cartesian product or all paths were checked.
    variations={'rail':(450,600,750),'park':(220,260,300),'halfwidth':(400,520,900),
                'body_scale':(.7,1,1.3),'cable':(18,30,50),'arm_width':(20,30,50),
                'head_stroke':(150,240,300),'bed_stroke':(150,240,300),
                'finished_height':(60,200,300)}
    sensitivity=[]
    for name,values in variations.items():
        for value,a,e in product(values,('H','B'),(False,True)):
            cases=[scene(m,a,e,replace(p,**{name:value}),True,'print',finished) for m in MODES for finished in (None,ASSIGNMENTS[m][0])]
            sensitivity.append({'parameter':name,'value':value,'architecture':a,'orientation':'E' if e else 'common',
                'mode_cases':len(cases),'first_witnesses_by_case':[{'mode':c['mode'],'finished_owner':c['finished_owner'],'witnesses':c['first_witnesses']} for c in cases],'stroke_failed_cases':sum(bool(c['failed_head_strokes']) or c['bed_stroke_failed'] for c in cases),
                'events':{k:sum(c['events'][k] for c in cases) for k in cases[0]['events']}})
    return {'units':'mm','scope':'Hypothetical full-length radial rails, affine box paths; no machine feasibility result',
            'parameters':asdict(p),'baseline':baseline,'sensitivity':sensitivity,'negative_fixtures':witnesses()}


def markdown(data):
    lines=['# D8 — generated analytical results','',
        'Generated by [d8_geometry.py](d8_geometry.py). Counts are event occurrences, not collision severity or probability.',
        'Every row remains **unresolved for real hardware**. Same synthetic XY geometry for H/B; E changes functional allocations only.',
        'Independent hull overlaps are conservative candidates; synchronized events are exact only for the stated affine boxes.','',
        '| Mode | Candidate | Orientation | Cases (both panel states) | Stroke-failed cases | Object events | Assembly events | Boundary events |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for m,a,e in product(MODES,('H','B'),('common','E')):
        cs=[c for c in data['baseline'] if (c['mode'],c['architecture'],c['orientation'])==(m,a,e)]
        sums=[sum(c['events'][k] for c in cs) for k in ('object','assembly','boundary')]
        lines.append(f'| {m} | {a} | {e} | {len(cs)} | {sum(bool(c["failed_head_strokes"]) or c["bed_stroke_failed"] for c in cs)} | '+ ' | '.join(map(str,sums))+' |')
    lines+=['','## One-factor-at-a-time sensitivity','',
        'Each row checks 16 enclosed cases: all eight modes live, then with first owner finished and object retained. Other parameters stay at baseline.',
        'These totals compare the same fixtures; they are not scores or complete mode certificates.','',
        '| Parameter | Value | Candidate | Orientation | Stroke-failed cases | Object events | Assembly events | Boundary events |',
        '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for s in data['sensitivity']:
        lines.append('| '+' | '.join(map(str,[s['parameter'],s['value'],s['architecture'],s['orientation'],s['stroke_failed_cases'],s['events']['object'],s['events']['assembly'],s['events']['boundary']]))+' |')
    return '\n'.join(lines)+'\n'


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    options=parser.add_mutually_exclusive_group()
    options.add_argument('--write',action='store_true')
    options.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=results(); encoded=json.dumps(data,indent=2,sort_keys=True)+'\n'
    root=Path(__file__).parent
    if args.check:
        assert (root/'d8-results.json').read_text()==encoded, 'stale JSON'
        assert (root/'d8-results.md').read_text()==markdown(data), 'stale Markdown'
        print('PASS: D8 generated JSON and Markdown match source')
    elif args.write:
        (root/'d8-results.json').write_text(encoded)
        (root/'d8-results.md').write_text(markdown(data))
    else: print(encoded,end='')
