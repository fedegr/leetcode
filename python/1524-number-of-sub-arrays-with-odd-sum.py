from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd_count, even_count = 0, 1
        result, current_sum = 0, 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                result += even_count
                odd_count += 1
            else:
                result += odd_count
                even_count += 1
            result %= MOD
        return result
