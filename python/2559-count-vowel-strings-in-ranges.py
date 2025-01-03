from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ('a', 'e', 'i', 'o', 'u')
        
        def match_criteria(word):
            return word[0] in vowels and word[-1] in vowels

        vowels_strings = [0 for _ in range(len(words) + 1)]

        for i, w in enumerate(words, 1):
            vowels_strings[i] += vowels_strings[i-1] + (1 if match_criteria(w) else 0)

        return [vowels_strings[e + 1] -  vowels_strings[s] for s, e in queries]
