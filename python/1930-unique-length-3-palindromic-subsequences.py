class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pos = dict()

        for i, c in enumerate(s):
            pos.setdefault(c, [i, i])[1] = i
        
        palindromes = set()
        for i, c in enumerate(s[1:-1], 1):
            for l, r in pos.values():
                if l < i < r:
                    palindromes.add(s[l]+c+s[r])
        
        return len(palindromes)
