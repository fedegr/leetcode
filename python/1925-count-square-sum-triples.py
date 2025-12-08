class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(a, n):
                s = (a**2 + b**2)
                c = int(s ** 0.5)
                if c > n:
                    break
                if c ** 2 == s:
                    count += 1

        return count * 2
