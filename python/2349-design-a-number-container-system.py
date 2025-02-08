import heapq 


class NumberContainers:

    def __init__(self):
        self.data = {}
        self.numbers = {}

    def change(self, index: int, number: int) -> None:
        old = self.data.get(index, None)

        if old == number:
            return
        
        self.data[index] = number

        if old is not None:
            _, deleted = self.numbers[old]
            deleted.add(index)
        
        ids, dels = self.numbers.setdefault(number, ([], set()))
        if index in dels:
            dels.remove(index)
        else:
            heapq.heappush(ids, index)
        

    def find(self, number: int) -> int:
        number_data = self.numbers.get(number, None)
        if number_data is None:
            return -1
        heap, deleted = number_data

        while heap and heap[0] in deleted:
            deleted.remove(heapq.heappop(heap))
        
        if len(heap) == 0:
            return -1
        
        return heap[0]
        



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)