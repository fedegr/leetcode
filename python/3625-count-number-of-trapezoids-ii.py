from fractions import Fraction
from itertools import combinations
from math import comb
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        segments = {}
        for (x0, y0), (x1, y1) in combinations(points, 2):
            group = None
            if x0 == x1:
                group = ('V', x0)
            elif y0 == y1:
                group = ('H', y0)
            else:
                d = 0
                y_cut = 0
                if x0 < x1:
                    d = Fraction((y1 - y0), (x1 - x0))
                    y_cut = - d * x0 + y0
                else:
                    d = Fraction((y0 - y1), (x0 - x1))
                    y_cut = -d * x1 + y1
                group = (d, y_cut)

            segment_data = segments \
                .setdefault(group[0], {}) \
                .setdefault(group[1], {})
            segment_data.setdefault('points', set()).update(((x0, y0), (x1, y1)))
            l = (y0 - y1)**2 + (x0 - x1)**2
            segment_data.setdefault('lengths', {})
            segment_data['lengths'][l] = segment_data['lengths'].get(l, 0) + 1
                    
        total = 0
        paral = 0
        for category, planes in segments.items():
            for plane0, plane1 in combinations(planes.values(), 2):
                total += comb(len(plane0['points']), 2) * comb(len(plane1['points']), 2)
                paral += sum(
                    c0 * c1
                    for s0, c0 in plane0['lengths'].items()
                    for s1, c1 in plane1['lengths'].items()
                    if s0 == s1
                )

        return total - paral // 2
