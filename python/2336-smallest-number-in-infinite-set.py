import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.data = []
        self.nums = set()

    def popSmallest(self) -> int:
        if len(self.data) > 0:
            ret = heapq.heappop(self.data)
            self.nums.remove(ret)
        else:
            ret = self.smallest
            self.smallest += 1
        return ret


    def addBack(self, num: int) -> None:
        if num >= self.smallest:
            return
        if num not in self.nums:
            self.nums.add(num)
            heapq.heappush(self.data, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)