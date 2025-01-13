class Solution:
    def minimumLength(self, s: str) -> int:
        reps = {}
        for c in s:
            reps[c] = reps.get(c, 0) + 1

        ans = len(s)
        for n in reps.values():
            if n < 3:
                continue
            ans -= ((n - 1) // 2) * 2
                
        return ans
