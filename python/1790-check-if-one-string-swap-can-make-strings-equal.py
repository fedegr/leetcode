class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(diff) != 2:
            return len(diff) == 0

        c1, c2 = diff

        return s1[c1] == s2[c2] and s1[c2] == s2[c1]
