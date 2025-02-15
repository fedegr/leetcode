from itertools import combinations


class Solution:
    def can_partition(self, n: int, target: int) -> Tuple[Tuple[int]]:
        s = str(n)
        for i in range(1, len(s)):
            for c in combinations(range(1, len(s)), i):
                partition_sum = 0
                prev = 0
                for l in c:
                    partition_sum += int(s[prev:l])
                    prev = l
                partition_sum += int(s[prev:])
                if partition_sum == target:
                    return True
        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_number = 1
        for i in range(2,n+1):
            sq = i * i
            if self.can_partition(sq, i):
                punishment_number += sq
        return punishment_number
