class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.last_zero = -1

    def add(self, num: int) -> None:
        prod = num
        if len(self.data) > 0 and self.data[-1] > 0:
            prod *= self.data[-1]
        if num == 0:
            self.last_zero = len(self.data)
        self.data.append(prod)

    def getProduct(self, k: int) -> int:
        pos = len(self.data) - k
        if pos <= self.last_zero:
            return 0
        elif pos - 1 == self.last_zero or pos == 0:
            return self.data[-1]
        return self.data[-1] // self.data[pos-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)