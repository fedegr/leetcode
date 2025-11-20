class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        points = sorted(intervals, key=lambda x: (x[1], -x[0]))
        last_point_0, last_point_1 = points[0][-1] - 1, points[0][-1]
        count = 2
        for (s, e) in points[1:]:
            if last_point_1 < s or (last_point_0 < s and last_point_1 == e):
                count += 2
                last_point_0, last_point_1 = e-1, e
            elif last_point_0 < s:
                count += 1
                last_point_0, last_point_1 = last_point_1, e
        return count
