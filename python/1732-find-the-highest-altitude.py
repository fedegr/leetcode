from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            if max_altitude < altitude:
                max_altitude = altitude
        
        return max_altitude
