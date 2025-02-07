class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = dict()
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        ans = 0
        for num, c in count.items():
            if num * 2 == k:
                ans += c // 2
                continue
            pair = k - num
            pair_c = count.get(pair, 0)
            ans += min(pair_c, c)
            count[num] = 0
            if pair_c != 0:
                count[pair] = 0
        
        return ans
