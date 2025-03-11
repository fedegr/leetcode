
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        unique = 0
        start = 0
        chars = {'a': 0, 'b': 0, 'c': 0}
        for end, c in enumerate(s):
            if c in chars:
                chars[c] += 1
                if chars[c] == 1:
                    unique += 1
                while s[start] not in chars or chars[s[start]] > 1:
                    if s[start] in chars:
                        chars[s[start]] -= 1
                    start += 1
                if unique == 3:
                    answer += (start + 1)
        return answer
