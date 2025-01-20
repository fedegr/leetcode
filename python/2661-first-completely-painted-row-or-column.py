from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = [len(mat[0]) for _ in mat]
        cols = [len(mat) for _ in mat[0]]

        arr_map = dict()
        for y, row in enumerate(mat):
            for x, val in enumerate(row):
                arr_map[val] = y*len(row) + x

        arr = [arr_map[val] for val in arr]

        for i, val in enumerate(arr):
            row_num = val // len(cols)
            rows[row_num] -= 1

            col_num = val % len(cols)
            cols[col_num] -= 1
            if rows[row_num] == 0 or cols[col_num] == 0:
                return i
        
        raise "Invalid data"
