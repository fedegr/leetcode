# 2405-optimal-partition-of-string

class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        partitions = 1
        for c in s:
            if c in chars:
                chars = set()
                partitions += 1
            chars.add(c)
        return partitions
