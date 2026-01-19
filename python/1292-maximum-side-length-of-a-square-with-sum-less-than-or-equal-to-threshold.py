from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefix_sums = [[0] * (len(mat[0]) + 1) for _ in range(len(mat)+1)]
        
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                prefix_sums[y+1][x+1] = mat[y][x] + prefix_sums[y][x+1] + prefix_sums[y+1][x] - prefix_sums[y][x]

        min_size = 0
        max_size = min(len(mat), len(mat[0]))

        best = 0
        while min_size <= max_size:
            size = (min_size + max_size) // 2
            if is_side_length(prefix_sums, size, threshold):
                best = size
                min_size = size + 1
            elif best < size - 1:
                max_size = size - 1
            else:
                break

        return best


def is_side_length(prefix_sums, size, threshold):
    for y in range(size, len(prefix_sums)):
        for x in range(size, len(prefix_sums[0])):
            val = prefix_sums[y][x] - prefix_sums[y-size][x] - prefix_sums[y][x-size] + prefix_sums[y-size][x-size]
            if val <= threshold:
                return True
    return False
            
# mat = [[8,8,8,8,8],[8,1,1,1,8],[8,1,1,1,8],[8,1,1,1,8],[8,8,8,8,8]]
# threshold = 9
