class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        start = 0
        end = len(height) - 1
        while start < end:
            water = min(height[start], height[end]) * (end - start)
            if max_water < water:
                max_water = water
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_water
