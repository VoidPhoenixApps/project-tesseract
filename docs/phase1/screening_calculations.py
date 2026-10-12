"""Reproduce Phase 1 scalar estimates; no hardware access or validation claims."""

from math import acos, degrees, pi, sqrt


def main():
    alpha, e_al, e_steel, b = 23.6e-6, 68300.0, 200000.0, 180.0
    print("Units: mm, N, MPa, K unless labeled. Analytical assumptions only.")
    for dt in (20, 40, 60, 80):
        print(f"Al growth at +{dt} K: {alpha*b*dt:.5f}")
    for t1, t2 in ((60, 60), (60, 20), (80, 80)):
        print(f"0.20 cold gap at +{t1}/+{t2} K: {0.2-alpha*b*(t1+t2)/2:.5f}")
    print(f"Steel pitch growth +20 K: {12e-6*180.2*20:.5f}")
    print(f"Al/steel differential +60 K: {(alpha-12e-6)*b*60:.5f}")
    print(f"Restrained Al stress +60 K: {e_al*alpha*60:.5f} MPa")
    for gradient in (1, 5):
        print(f"Free gradient bow {gradient} K, 4 mm plate: {alpha*gradient/4*b*b/8:.5f}")
    for thickness in (3, 4, 6):
        inertia = b*thickness**3/12
        delta = 20*b**3/(48*e_al*inertia)
        print(f"Plate {thickness} mm: I={inertia:.2f} mm^4, delta={delta:.5f}")
    for diameter in (12, 12.7):
        inertia = pi*diameter**4/64
        delta = 10*400**3/(48*e_steel*inertia)
        print(f"Rod {diameter} mm: I={inertia:.2f} mm^4, simple={delta:.5f}, cantilever={16*delta:.5f}")
    print(f"Latch couple: {50*0.04:.2f} N m; reaction={50*40/120:.5f} N")
    print(f"Angular budget: {degrees(.05/90):.5f} deg; Ktheta={2/(.05/90):.2f} N m/rad")
    print(f"Uncertainty example U(k=2): {2*sqrt(.003**2+.004**2+.002**2):.5f}")
    for coordinate in (130, 90.1):
        radius = sqrt(2)*(300-coordinate)
        elbow = degrees(acos((radius**2-180**2-160**2)/(2*180*160)))
        print(f"Arm endpoint ({coordinate},{coordinate}): radius={radius:.2f}, elbow={elbow:.2f} deg")


if __name__ == "__main__":
    main()
