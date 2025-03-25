from typing import List


def lines_without_overlap(rectangles: List[List[int]], y: bool=False) -> bool:
    component = 1 if y else 0
    rectangles.sort(key=lambda x: (x[component], x[component+2]))

    cuts = 0
    last_end = rectangles[0][component+2]
    for i in range(1, len(rectangles)):
        rect = rectangles[i]
        start = rect[component]
        end = rect[component + 2]
        if start >= last_end:
            last_end = end
            cuts += 1
            if cuts == 2:
                return True
        else:
            last_end = max(last_end, end)

    return False

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return lines_without_overlap(rectangles) or lines_without_overlap(rectangles, y=True)
