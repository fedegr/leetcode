from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        sorted_spells = [(s, i) for i, s in enumerate(spells)]
        sorted_spells.sort(reverse=True)
        potion_id = 0
        answer = [0 for _ in range(len(spells))]
        for s, i in sorted_spells:
            while potion_id < len(potions) and s * potions[potion_id] < success:
                potion_id += 1
            answer[i] = len(potions) - potion_id
        return answer
