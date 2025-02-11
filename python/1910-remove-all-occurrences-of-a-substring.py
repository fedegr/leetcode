from collections import deque


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = deque()

        for c in s:
            stack.append(c)
            if len(stack) >= len(part) and all(stack[i-len(part)] == part_i for i, part_i in enumerate(part)):
                for _ in range(len(part)):
                    stack.pop()

        return ''.join(stack)
