# 1657-determine-if-two-strings-are-close


def count_occurrences(word):
    occurrences = {}
    for c in word:
        occurrences[c] = occurrences.get(c, 0) + 1
    return occurrences


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        occurrences1 = count_occurrences(word1)
        occurrences2 = count_occurrences(word2)

        return (
            set(occurrences1.keys()) == set(occurrences2.keys()) and 
            sorted(occurrences1.values()) == sorted(occurrences2.values())
        )
