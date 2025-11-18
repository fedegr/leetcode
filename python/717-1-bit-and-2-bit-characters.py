from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        iterator = reversed(bits)
        val = next(iterator)
        if val == 1:
            return False
        
        ones = 0
        for b in iterator:
            if b == 0:
                break
            ones += 1

        return ones % 2 == 0
