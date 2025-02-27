def lenLongestFibSubseqBruteforce(arr: List[int]) -> int:
    values = set(arr)
    best = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            a = arr[i]
            b = arr[j]
            size = 2
            while a + b in values:
                a, b = b, a + b
                size += 1
            
            if size > best:
                print(arr[i], arr[j])
                best = size
    if best < 3:
        best = 0
    
    return best


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        return lenLongestFibSubseqBruteforce(arr)
                