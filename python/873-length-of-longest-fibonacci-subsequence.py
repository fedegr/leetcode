from typing import List


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


def lenLongestFibSubseqDP(arr: List[int]) -> int:
    idx = { n: i for i, n in enumerate(arr) }
    best = 0
    longest = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            b = arr[i]
            c = arr[j]
            a = c - b
            prev = idx.get(a, None)
            if prev is not None and a < b:
                longest[i][j] = longest[prev][i] + 1
                best = max(best, longest[i][j])
            else:
                longest[i][j] = 2

    if best < 3:
        best = 0
    
    return best



class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        return lenLongestFibSubseqDP(arr)
                