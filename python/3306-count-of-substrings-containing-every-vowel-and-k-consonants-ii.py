from collections import defaultdict

VOWELS = ('a', 'e', 'i', 'o', 'u')

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        repetitions = defaultdict(lambda: 0)
        vowels = 0
        consonants = 0
        
        combinations = 1
        answer = 0
        start = 0
        for i, c in enumerate(word):
            first_appearence = repetitions[c] == 0
            repetitions[c] += 1
            
            if c in VOWELS:
                if first_appearence:
                    vowels += 1
            else:
                consonants += 1
                while consonants > k and start <= i:
                    remove = word[start]
                    repetitions[remove] -= 1
                    if remove in VOWELS:
                        if repetitions[remove] == 0:
                            vowels -= 1
                    else:
                        consonants -= 1
                        combinations = 1
                    start += 1

            while start < len(word) and word[start] in VOWELS and repetitions[word[start]] > 1:
                repetitions[word[start]] -= 1
                start += 1
                combinations += 1

            if consonants == k and vowels == 5:
                answer += combinations
        return answer
