from typing import List
import heapq


def shift(char, amount):
    return chr((ord(char) + amount - 97) % 26 + 97)


class Solution:
    def shiftingLetterNaive(self, s: str, shifts: List[List[int]]) -> str:
        shifts.sort()

        next_shift = 0
        current_shifts = []
        consolidated_shift = 0
        answer = [c for c in s]
        for i, c in enumerate(s):

            while next_shift < len(shifts) and i == shifts[next_shift][0]:
                _, end, direction = shifts[next_shift]
                amount = -1 if direction == 0 else 1
                next_shift += 1
                consolidated_shift += amount
                heapq.heappush(current_shifts, (end, amount))

            answer[i] = shift(c, consolidated_shift)

            while len(current_shifts) > 0 and current_shifts[0][0] == i:
                _, amount = heapq.heappop(current_shifts)
                consolidated_shift -= amount

        return "".join(answer)

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            change = -1 if direction == 0 else 1
            changes[start] += change
            changes[end + 1] -= change

        current_shift = 0
        answer = [None for c in s]
        for i, c in enumerate(s):
            current_shift += changes[i]
            answer[i] = shift(c, current_shift)

        return "".join(answer)
