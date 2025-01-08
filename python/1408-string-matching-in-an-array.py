from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for i, word in enumerate(words):
            for j, container in enumerate(words):
                if i != j and word in container:
                    answer.append(word)
                    break
        return answer
