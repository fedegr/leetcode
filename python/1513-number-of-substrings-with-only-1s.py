class Solution:
    def numSub(self, s: str) -> int:
        total = 0
        count = 0
        for i, c in enumerate(s):
            if c == '1':
                count += 1
            else:
                num = (count * (count+1)) // 2
                total += num
                total %= 1000000007
                count = 0

        if count > 0:
            num = (count * (count+1)) // 2
            total += num
            total %= 1000000007
        return total
