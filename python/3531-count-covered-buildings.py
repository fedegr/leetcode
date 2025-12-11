from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xs = {}
        ys = {}

        for (x, y) in buildings:
            min_y, max_y = ys.get(x, (y, y))
            ys[x] = (min(min_y, y), max(max_y, y))

            min_x, max_x = xs.get(y, (x, x))
            xs[y] = (min(min_x, x), max(max_x, x))

        
        return sum(
            1
            for x, y in buildings
            if (
                xs[y][0] < x and x < xs[y][1] and
                ys[x][0] < y and y < ys[x][1]
            )
        )
