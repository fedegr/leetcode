from typing import List

def is_prefix_and_suffix(w1, w2):
    return w2.startswith(w1) and w2.endswith(w1)

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i, word_i in enumerate(words):
            for j, word_j in enumerate(words[i+1:], start=i+1):
                if is_prefix_and_suffix(word_i, word_j):
                    count += 1
        
        return count
