from collections import deque
from functools import cmp_to_key

def construct_distanced_sequence_recursive(result, used, n, index):
    while index < len(result) and result[index] is not None:
        index += 1
    
    if index == len(result):
        return True
    
    for i in range(n, 0, -1):
        if used[i]:
            continue

        if i == 1:
            result[index] = 1
            used[1] = True
            if construct_distanced_sequence_recursive(result, used, n, index + 1):
                return True
            result[index] = None
            used[1] = False
        elif index + i < len(result) and result[index + i] is None:
            result[index] = i
            result[index + i] = i
            used[i] = True
            if construct_distanced_sequence_recursive(result, used, n, index + 1):
                return True
            result[index] = None
            result[index + i] = None
            used[i] = False

    return False
    

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [None] * (2 * n - 1)
        used = [False] * (n + 1)
        construct_distanced_sequence_recursive(result, used, n, 0)
        return result
