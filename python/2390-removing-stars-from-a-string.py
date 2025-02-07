from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        data = deque()
        for c in s:
            if c == '*' and len(data) > 0:
                data.pop()
            else:
                data.append(c)
        return ''.join(data)
