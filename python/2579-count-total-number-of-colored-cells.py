def colored_cells_recursive(n: int) -> int:
        if n == 1:
            return 1
        return colored_cells_recursive(n-1) + n * 2 + (n - 2) * 2

def colored_cells(n: int) -> int:
        # triangle_big = n * (n + 1) / 2
        # triangle_small = (n - 1) * (n - 2) / 2
        # result = triangle_big * 2 - 1 + triangle_small * 2 
        return n * (n + 1) - 1 + (n - 1) * (n - 2)

class Solution:
    def coloredCells(self, n: int) -> int:
        return colored_cells(n)