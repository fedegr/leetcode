class Solution:
    def numberOfWays(self, corridor: str) -> int:
        start = None
        seats = 0
        MOD = 10**9 + 7
        result = 1
        for i, c in enumerate(corridor):
            if c == 'S':
                if seats < 2:
                    seats += 1
                    if seats == 2:
                        start = i
                else:
                    result = (result * (i - start)) % MOD
                    seats = 1
                    start = None

        if start is None:
            return 0
        
        return result
