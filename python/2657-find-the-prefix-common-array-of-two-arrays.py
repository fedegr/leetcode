class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = [None] * len(A)
        c[0] = 1 if A[0] == B[0] else 0
        prev_a, prev_b = {A[0]}, {B[0]}
 
        for i in range(1, len(A)):
            c[i] = c[i-1]
            if A[i] == B[i]:
                c[i] += 1 
            else:
                if A[i] in prev_b:
                    c[i] += 1
                if B[i] in prev_a:
                    c[i] += 1
            prev_a.add(A[i])
            prev_b.add(B[i])
        
        return c
