class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) < 1:
            return 0

        zeros = [0]
        ones = [0]
        for i in range(len(s)):
            zeros.append(zeros[-1] + (1 if s[i] == '0' else 0))
            ones.insert(0, ones[0] + (1 if s[-i-1] == '1' else 0))
        
        return max(map(sum, zip(zeros[1:-1], ones[1:-1])))