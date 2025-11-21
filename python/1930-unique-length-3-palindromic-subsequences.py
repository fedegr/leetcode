class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pos = dict()

        for i, c in enumerate(s):
            pos.setdefault(c, [i, i])[1] = i
        
        count = 0
        for l, r in pos.values():
            count += len(set(s[l+1:r]))
        
        return count
