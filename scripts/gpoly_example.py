# -*- coding: utf-8 -*-
"""Check of the example in Section III of the Supplementary Material.

The plant has one furnace and one caster, heat time d = 2, turnaround g = 0, casting time c = 3, idle limit b = 1 and
waiting limit w = 1. At the notice t = 0 the furnace is idle, no ladle is waiting, and the cast in progress ends at
t = 1. A heat started at s runs in slots s, ..., s + d - 1 and taps at s + d. A cast started at z occupies the caster
until z + c, and the next cast starts in [z + c, z + c + b]. The ladle of each heat is cast within w slots of its tap,
first in, first out. The window starts at the notice, and its first three blocks are the slots 0-2, 3-5 and 6-8.

The script enumerates the schedules, prints the block loads of the first three blocks in units of P/3, the vertices
and edges of their convex hull, and the value of l1 + 2 l2 + l3 at every load vector.

Usage: python gpoly_example.py   (requires NumPy and SciPy)
"""
import itertools

import numpy as np
from scipy.spatial import ConvexHull

D, G, C, B, W = 2, 0, 3, 1, 1
N_CASTS = 5          # five casts reach past slot 8, so every load vector of the first three blocks appears
loads = set()


def extend(cast_end, prev_start, starts, depth):
    """cast_end: end slot of the previous cast; prev_start: start of the previous heat (None before the first)."""
    if depth == 0:
        occupied = [0] * 9
        for s in starts:
            for t in range(s, s + D):
                if t < 9:
                    occupied[t] += 1
        loads.add((sum(occupied[0:3]), sum(occupied[3:6]), sum(occupied[6:9])))
        return
    for z in range(cast_end, cast_end + B + 1):          # start of the next cast
        for tap in range(z - W, z + 1):                    # tap of its ladle, cast within W slots
            s = tap - D                                    # start of that heat
            if s < 0:
                continue
            if prev_start is not None and s < prev_start + D + G:
                continue                                   # the furnace is still busy
            extend(z + C, s, starts + [s], depth - 1)


extend(1, None, [], N_CASTS)
points = sorted(loads)
print("load vectors (units of P/3) and l1 + 2 l2 + l3:")
for p in points:
    print("  ", p, p[0] + 2 * p[1] + p[2])

P = np.array(points, dtype=float)
hull = ConvexHull(P)
vertex_ids = sorted(set(hull.vertices))
print("hull vertices:", [points[i] for i in vertex_ids])
print("hull edges and their directions:")
for a, b in itertools.combinations(vertex_ids, 2):
    mid = (P[a] + P[b]) / 2
    on = [k for k, eq in enumerate(hull.equations) if abs(eq[:3] @ mid + eq[3]) < 1e-9]
    normals = np.unique(np.round(hull.equations[on, :3], 9), axis=0)
    if len(normals) >= 2:                                  # the midpoint lies on two facets, so ab is an edge
        direction = tuple(int(x) for x in P[b] - P[a])
        print("  ", points[a], "->", points[b], "direction", direction)
