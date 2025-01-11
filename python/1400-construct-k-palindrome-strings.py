class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        rep = {}
        for c in s:
            rep[c] = rep.get(c, 0) + 1

        print(rep)

        odds_count = 0
        sum_evens = 0
        for c, n in rep.items():
            if n % 2 == 1:
                rep[c] -= 1
                odds_count += 1
                n -= 1
            sum_evens += n

        return odds_count == k or (odds_count < k and sum_evens >= k - odds_count)