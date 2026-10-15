"""D2 screening, millimetres. Standard library only; no machine or vendor model.
Closed AABBs: touching is conflict. Linear segment CCD is exact for these boxes;
workspace hull overlap is conservative and cannot establish physical contact.
"""
from dataclasses import dataclass, asdict
from itertools import product, combinations
import json
import math


@dataclass(frozen=True)
class Box:
    lo: tuple
    hi: tuple

    def __post_init__(self):
        if len(self.lo) != 3 or len(self.hi) != 3 or any(
            not math.isfinite(a) or not math.isfinite(b) or a > b
            for a, b in zip(self.lo, self.hi)
        ):
            raise ValueError('finite ordered XYZ bounds required')

    def move(self, p):
        if len(p) != 3 or not all(math.isfinite(x) for x in p):
            raise ValueError('finite XYZ translation required')
        return Box(tuple(a+b for a,b in zip(self.lo,p)), tuple(a+b for a,b in zip(self.hi,p)))

    def inflate(self, c):
        if not math.isfinite(c) or c < 0:
            raise ValueError('nonnegative finite reservation required')
        return Box(tuple(x-c for x in self.lo), tuple(x+c for x in self.hi))

    def overlaps(self, b):
        return all(a <= d and c <= e for a,e,c,d in zip(self.lo,self.hi,b.lo,b.hi))

    def contains(self, b):
        return all(a <= c and d <= e for a,e,c,d in zip(self.lo,self.hi,b.lo,b.hi))


def hull(boxes):
    boxes = list(boxes)
    if not boxes:
        raise ValueError('empty geometry is not evidence')
    return Box(tuple(min(b.lo[i] for b in boxes) for i in range(3)),
               tuple(max(b.hi[i] for b in boxes) for i in range(3)))


def orient(p, head, mirrored=True):
    """D1: A, mirror-X(A), rotate180(B), rotate180(A); fixed to carriage."""
    if head not in (1,2,3,4):
        raise ValueError('head must be 1..4')
    sx,sy = {1:(1,1),2:(-1,1),3:(1,-1),4:(-1,-1)}[head] if mirrored else (1,1)
    return p[0]*sx,p[1]*sy,p[2]


def oriented(b, head, mirrored=True):
    points = [orient(p,head,mirrored) for p in product(*zip(b.lo,b.hi))]
    return hull(Box(p,p) for p in points)


def sweep(b, points):
    """Conservative for fixed orientation and piecewise-linear translation only."""
    if len(points) < 2:
        raise ValueError('path requires at least two vertices')
    return hull(b.move(p) for p in points)


def ccd(a, a0, a1, b, b0=(0,0,0), b1=(0,0,0)):
    """Continuous overlap time interval on a synchronized linear segment, or None."""
    aa,bb = a.move(a0),b.move(b0)
    a.move(a1); b.move(b1)  # validate endpoints, including stationary objects
    enter,leave = 0.0,1.0
    for i in range(3):
        v = (a1[i]-a0[i])-(b1[i]-b0[i])
        low,high = bb.lo[i]-aa.hi[i],bb.hi[i]-aa.lo[i]
        if v == 0:
            if low > 0 or high < 0:
                return None
        else:
            t0,t1 = sorted((low/v,high/v))
            enter,leave = max(enter,t0),min(leave,t1)
            if enter > leave:
                return None
    return (enter,leave)


def path_hits(body, points, obstacle):
    if len(points) < 2:
        raise ValueError('path requires two vertices')
    return [i for i,(a,b) in enumerate(zip(points,points[1:])) if ccd(body,a,b,obstacle) is not None]


MODES = {
    'S': ((1,),(2,),(3,),(4,)), 'R': ((1,2),(3,4)), 'C': ((1,3),(2,4)),
    'M12': ((1,2),(3,),(4,)), 'M34': ((3,4),(1,),(2,)),
    'M13': ((1,3),(2,),(4,)), 'M24': ((2,4),(1,),(3,)), 'J': ((1,2,3,4),),
}
# Injective assignments; each pair/full region has ONE head. No cooperative union.
ASSIGNMENTS = {'S':(1,2,3,4),'R':(1,3),'C':(1,2), 'M12':(1,3,4),
               'M34':(3,1,2),'M13':(1,2,4),'M24':(2,1,3),'J':(1,)}


@dataclass(frozen=True)
class Parameters:
    side: float = 180                 # A: nominal requirement, not printable size
    gap: float = 40                   # C: separation gap
    joined_gap: float = 0             # C: ideal seam; not demonstrated hot seam
    margin: float = 5                 # C: illustrative OUTER region inset only
    head_z_travel: float = 300         # C: hypothetical usable nozzle stroke
    bed_z_travel: float = 200          # C: alternative downward travel
    object_height: float = 200         # C: no approved build height exists
    beam_width: float = 30
    beam_depth: float = 30
    beam_offset: float = 80
    beam_level: float = 320
    beam_spacing: float = 40
    frame_inner: float = 320          # half width of hypothetical clear enclosure
    frame_reservation: float = 20
    cable_radius: float = 30
    filament_radius: float = 40
    clearance: float = 2              # C: numerical sensitivity, NOT safe stop distance
    park: float = 260                 # absolute nozzle X/Y in corner parking
    nozzle_offset: tuple = (20,-20,-50)  # A local nozzle minus carriage
    body_lo: tuple = (-50,-8,10)
    body_hi: tuple = (8,50,70)

    def __post_init__(self):
        for k,v in asdict(self).items():
            if isinstance(v,(int,float)) and (not math.isfinite(v) or v < 0):
                raise ValueError('nonnegative finite '+k+' required')
        if self.side <= 0 or self.margin*2 >= self.side:
            raise ValueError('invalid side or margin')
        Box(self.body_lo,self.body_hi)
        if len(self.nozzle_offset) != 3 or not all(math.isfinite(x) for x in self.nozzle_offset):
            raise ValueError('invalid nozzle offset')


def beds(mode,p):
    """Hypothetical final XY layouts. Outer corners spread; joined edges at zero.
    Four mixed layouts keep the opposite two singles separated. Not transition paths.
    """
    if mode not in MODES:
        raise ValueError('unknown mode')
    xy={1:(-1,1),2:(1,1),3:(-1,-1),4:(1,-1)}
    result={}
    for i,(sx,sy) in xy.items():
        gx = p.joined_gap if mode in ('R','J') or (mode=='M12' and i in (1,2)) or (mode=='M34' and i in (3,4)) else p.gap
        gy = p.joined_gap if mode in ('C','J') or (mode=='M13' and i in (1,3)) or (mode=='M24' and i in (2,4)) else p.gap
        cx,cy=sx*(p.side+gx)/2,sy*(p.side+gy)/2
        result[i]=Box((cx-p.side/2,cy-p.side/2,0),(cx+p.side/2,cy+p.side/2,0))
    return result


def regions(mode,p):
    bs=beds(mode,p)
    out=[]
    for group in MODES[mode]:
        b=hull(bs[i] for i in group)
        out.append(Box((b.lo[0]+p.margin,b.lo[1]+p.margin,0),
                       (b.hi[0]-p.margin,b.hi[1]-p.margin,0)))
    return out


def nozzle_reach(carriage,head,p,mirrored=True):
    return carriage.move(orient(p.nozzle_offset,head,mirrored))


def required_carriage(region,head,p,mirrored=True):
    return region.move(tuple(-x for x in orient(p.nozzle_offset,head,mirrored)))


def components(head,p,mirrored=True):
    """C geometry: boxes about nozzle, no purchased-component representation."""
    raw={'body':Box(p.body_lo,p.body_hi),
         'hotend':Box((-6,-6,0),(6,6,20)),
         'probe':Box((-25,-10,2),(-15,0,25)),
         'carriage':Box((-40,5,35),(0,35,65)),
         'cable':Box((-50-p.cable_radius,15,30),(-40,35,100)),
         'filament':Box((-40-p.filament_radius,20,60),(-20,40,130))}
    return {name:oriented(b,head,mirrored) for name,b in raw.items()}


def footprint_sweep(b,region,z):
    return hull(b.move((x,y,z)) for x,y in product((region.lo[0],region.hi[0]),(region.lo[1],region.hi[1])))


def assembly(head,p,region,z,topology,mirrored=True):
    """Bounding operational volumes, including full beam and descending Z column.
    This is a rejection screen of two explicit thought experiments, not all A/B.
    """
    if topology not in ('moving-bridge','stacked-bridge'):
        raise ValueError('unsupported kinematics')
    out={k:footprint_sweep(b,region,z) for k,b in components(head,p,mirrored).items()}
    bz=z+p.beam_offset if topology=='moving-bridge' else p.beam_level+(head-1)*p.beam_spacing
    out['beam']=Box((-p.park-30,region.lo[1]-p.beam_width/2,bz),
                    (p.park+30,region.hi[1]+p.beam_width/2,bz+p.beam_depth))
    # Variable-length drop is conservatively enclosed over the job's fixed layer.
    if bz < z+70:
        raise ValueError('beam below head attachment')
    out['Z-column']=footprint_sweep(oriented(Box((-40,5,35),(0,35,bz+p.beam_depth-z)),head,mirrored),region,z)
    return out


def mode_screen(mode,p,topology='moving-bridge',mirrored=True):
    rs=regions(mode,p); active=ASSIGNMENTS[mode]
    heights=(10,150,60,200)[:len(active)]
    machines={}
    # Shared reference travel for the thought experiment: center can reach [-240,240].
    travel=Box((-240,-240,50),(240,240,p.head_z_travel+50))
    reaches=[]
    park_reaches={}
    park_carriages={}
    for h,r,z in zip(active,rs,heights):
        target=Box((r.lo[0],r.lo[1],0),(r.hi[0],r.hi[1],p.object_height))
        reaches.append(nozzle_reach(travel,h,p,mirrored).contains(target))
        machines[h]=assembly(h,p,r,z,topology,mirrored)
    for h in set((1,2,3,4))-set(active):
        sx,sy={1:(-1,1),2:(1,1),3:(-1,-1),4:(1,-1)}[h]
        park=Box((sx*p.park,sy*p.park,0),(sx*p.park,sy*p.park,0))
        park_z = p.head_z_travel if topology=='moving-bridge' else min(p.head_z_travel,p.beam_level+(h-1)*p.beam_spacing-100)
        park_nozzle=Box((sx*p.park,sy*p.park,park_z),(sx*p.park,sy*p.park,park_z))
        park_carriages[h]=asdict(required_carriage(park_nozzle,h,p,mirrored))
        park_reaches[h]=nozzle_reach(travel,h,p,mirrored).contains(park_nozzle)
        machines[h]=assembly(h,p,park,park_z,topology,mirrored)
    candidates=[]
    for a,b in combinations(sorted(machines),2):
        for na,ba in machines[a].items():
            for nb,bb in machines[b].items():
                if ba.inflate(p.clearance).overlaps(bb):
                    candidates.append(f'H{a}:{na}/H{b}:{nb}')
    # Other jobs' objects, not the intended own deposition contact.
    objects=[Box((r.lo[0],r.lo[1],0),(r.hi[0],r.hi[1],z)) for r,z in zip(rs,heights)]
    obj_hits=[]
    for h,parts in machines.items():
        for j,(owner,obj) in enumerate(zip(active,objects)):
            if owner==h:
                continue
            for name,b in parts.items():
                if b.inflate(p.clearance).overlaps(obj):
                    obj_hits.append(f'H{h}:{name}/job{j+1}')
    # Coarse bed mechanisms stay below datum; frame inner box reserves panels/nodes.
    mechanisms={i:Box((b.lo[0]-5,b.lo[1]-5,-40),(b.hi[0]+5,b.hi[1]+5,-5)) for i,b in beds(mode,p).items()}
    mech_hits=[f'H{h}:{n}/bed{i}' for h,parts in machines.items() for n,b in parts.items()
               for i,m in mechanisms.items() if b.inflate(p.clearance).overlaps(m)]
    inner=p.frame_inner-p.frame_reservation
    enclosure=Box((-inner,-inner,-50),(inner,inner,600))
    outside=[f'H{h}:{n}' for h,parts in machines.items() for n,b in parts.items() if not enclosure.contains(b.inflate(p.clearance))]
    return {'mode':mode,'groups':MODES[mode],'heads':active,'heights_mm':heights,
            'nominal_nozzle_reach':reaches,'park_nozzle_reach':park_reaches,
            'park_required_carriage_mm':park_carriages,'region_bounds_mm':[asdict(r) for r in rs],
            'carriage_bounds_at_z0_mm':[asdict(required_carriage(r,h,p,mirrored)) for h,r in zip(active,rs)],
            'machine_overlap_candidates':candidates,'other_object_candidates':obj_hits,
            'bed_mechanism_candidates':mech_hits,'enclosure_outside':outside,
            'classification':'UNRESOLVED' if all(reaches) and all(park_reaches.values()) else 'REACH_REJECTED',
            'reason':'Envelope candidates are not physical contact proof; fixed supports, belts, deformation, actual paths and stop bounds remain unverified.'}


def eligibility(mode,architecture,p):
    """Functional reach matching, deliberately independent of assembly screening."""
    rs=regions(mode,p)
    local=list(beds(mode,p).values())
    global_box=hull(local)
    capacities={'local':local,'local+fifth':local+[global_box],
                'extended':[global_box]*4,'single-toolchanger':[global_box]}
    if architecture not in capacities:
        return 'UNRESOLVED'
    caps=capacities[architecture]
    def assign(index,used):
        if index==len(rs): return True
        return any(c.contains(rs[index]) and assign(index+1,used|{i}) for i,c in enumerate(caps) if i not in used)
    return 'REACH_ONLY' if assign(0,set()) else 'FUNCTION_REJECTED'


def classification(geometry_complete,kinematics_known,conflict):
    if not geometry_complete or not kinematics_known: return 'UNRESOLVED'
    return 'BOX_CONFLICT' if conflict else 'MODEL_CLEAR_ONLY'


def results():
    p=Parameters()
    body=Box((-5,-5,0),(5,5,20))
    obstacle=Box((-2,-10,0),(2,10,100))
    path=[(-30,0,10),(30,0,10)]
    return {'units':'mm','status':'synthetic analytical screening; no physical feasibility pass',
        'parameters_C_except_nominal_side_A':asdict(p),
        'functional_matrix':{m:{a:eligibility(m,a,p) for a in ('local','local+fifth','extended','single-toolchanger')} for m in MODES},
        'screens':{t:[mode_screen(m,p,t) for m in MODES] for t in ('moving-bridge','stacked-bridge')},
        'midpath_witness':{'endpoint_conflicts':[body.move(x).overlaps(obstacle) for x in path],
                           'collision_time_interval':ccd(body,*path,obstacle)},
        'stack_separation_needed_mm':[{'height_divergence':h,'beam_depth':d,'minimum_offset_strictly_greater_than':h+d+p.clearance} for h in (100,200,300) for d in (20,30,50)],
        'mirrored_seam_sensitivity':[{'body_outward':out,'body_inward':inside,'clearance':c,
            'mirrored_min_nozzle_spacing_strictly_greater_than':2*inside+c,
            'common_orientation_min_spacing_strictly_greater_than':out+inside+c,
            'outer_body_reservation_mirrored':out,'outer_body_reservation_common_right':inside}
            for out in (35,50,65) for inside in (5,8,15) for c in (0,2,5)],
        'parking_cable_sensitivity':[{'park_nozzle':park,'outward_with_cable':50+r,
              'required_frame_halfwidth':park+50+r+p.clearance+p.frame_reservation}
              for park in (220,260,300) for r in (18,30,50)],
        'gap_sensitivity':[{'gap':gap,'mode':m,'region_xy_sizes':[[b.hi[i]-b.lo[i] for i in (0,1)] for b in regions(m,Parameters(gap=gap))]} for gap in (20,40,80) for m in MODES]}


if __name__=='__main__':
    print(json.dumps(results(),indent=2,sort_keys=True))
