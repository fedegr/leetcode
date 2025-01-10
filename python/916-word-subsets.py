from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        universal_chars = dict()
        for word in words2:
            cs = {}
            for c in word:
                cs[c] = cs.get(c, 0) + 1
            
            for c, n in cs.items():
                if universal_chars.get(c, 0) < n:
                    universal_chars[c] = n
        
        universal_words = []
        for word in words1:
            cs = {}
            for c in word:
                cs[c] = cs.get(c, 0) + 1
            
            is_universal_word = True
            for c, n in universal_chars.items():
                if cs.get(c, 0) < n:
                    is_universal_word = False
                    break
            
            if is_universal_word:
                universal_words.append(word)
        
        return universal_words
            