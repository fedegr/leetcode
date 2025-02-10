from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        chars = deque()
        for c in s:
            if '0' <= c <= '9' and len(chars) > 0:
                chars.pop()
            else:
                chars.append(c)
        
        return ''.join(chars)
