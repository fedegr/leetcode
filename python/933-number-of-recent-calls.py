from collections import deque


class RecentCounter:
    def __init__(self):
        self.recent = deque()

    def ping(self, t: int) -> int:
        while len(self.recent) > 0 and self.recent[0] < t - 3000:
            self.recent.popleft()
        self.recent.append(t)
        
        return len(self.recent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)