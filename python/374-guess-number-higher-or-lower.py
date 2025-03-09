# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 0
        upper = n

        while lower <= upper:
            value = (lower + upper) // 2
            result = guess(value)
            if result == 0:
                return value
            if result == -1:
                upper = value - 1
            if result == 1:
                lower = value + 1

        return None
    