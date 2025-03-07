from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for _ in range(0, right+1)]
        primes[0] = False
        primes[1] = False
        i = 2
        while i * i <= right:
            if primes[i]:
                n = 2
                while i * n <= right:
                    primes[i * n] = False
                    n += 1
            i += 1

        last_prime = None
        best = (-1, -1)
        best_diff = right
        for i in range(left, right+1):
            if not primes[i]:
                continue
            if last_prime is not None:
                best_diff, best = min((best_diff, best), (i - last_prime, (last_prime, i)))
            last_prime = i

        return best
        