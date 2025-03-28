# 1492-the-kth-factor-of-n

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = 0
        for i in range(1, n+1):
            if n % i == 0:
                factors += 1
                if factors == k:
                    return i

        return -1
