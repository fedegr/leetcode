class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        spots = 0
        empty_start = 0
        for i, f in enumerate(flowerbed):
            if f == 1:
                spots += (i - empty_start) // 2
                # print(i, empty_start, spots)
                if spots >= n:
                    return True
                empty_start = i + 2
        spots += (i - empty_start + 2) // 2
        # print(i, empty_start, spots)
        return spots >= n
