from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        previous_color = None
        current_group_size = 0
        answer = 0
        for i in range(0, len(colors) + k - 1):
            c = colors[i % len(colors)]
            if c == previous_color:
                current_group_size = 0
            previous_color = c
            current_group_size += 1
            if current_group_size >= k:
                answer += 1
        return answer
                