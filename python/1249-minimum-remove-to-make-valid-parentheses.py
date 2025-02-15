from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        invalid = [False] * len(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    invalid[i] = True
        while stack:
            invalid[stack.pop()] = True
        
        result = ""
        for i, c in enumerate(s):
            if invalid[i]:
                continue
            result += c
        return result
