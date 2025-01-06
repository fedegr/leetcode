from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        index_sum = [0] * len(boxes)
        balls_sum = [0] * len(boxes)
        answer = [0] * len(boxes)

        for i, b in enumerate(boxes):
            index_sum[i] = (index_sum[i-1] if i > 0 else 0) + (i if b == "1" else 0)
            balls_sum[i] = (balls_sum[i-1] if i > 0 else 0) + (1 if b == "1" else 0)
        
        for i in range(0, len(boxes)):
            if i > 0:
                answer[i] += balls_sum[i-1] * i - index_sum[i-1]
            if i < len(boxes) - 1:
                answer[i] += (index_sum[-1] - index_sum[i]) - (balls_sum[-1] - balls_sum[i]) * i

        return answer
