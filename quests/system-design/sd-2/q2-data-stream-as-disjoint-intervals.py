from bisect import bisect

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        pos = bisect(self.intervals, value, key=lambda x: x[0])

        prev_value = self.intervals[pos-1][1] if pos > 0 else value - 2
        next_value = self.intervals[pos][0] if pos < len(self.intervals) else value + 2

        if prev_value >= value - 1 and next_value == value + 1:
            self.intervals[pos-1][1] = self.intervals[pos][1]
            self.intervals.pop(pos)
        elif prev_value >= value - 1:
            self.intervals[pos-1][1] = max(self.intervals[pos-1][1], value)
        elif next_value <= value + 1:
            self.intervals[pos][0] = value
        else:
            self.intervals.insert(pos, [value, value])
            
    def getIntervals(self) -> List[List[int]]:
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
