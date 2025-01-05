class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(c):
            return c in ('a', 'e', 'i', 'o', 'u')

        vowels = sum([1 if is_vowel(c) else 0 for c in s[:k]])
        max_vowels = vowels
        for i in range(1, len(s) - k + 1):
            vowels = (
                vowels 
                - (1 if is_vowel(s[i - 1]) else 0)
                + (1 if is_vowel(s[i + k - 1]) else 0)
            )
            if vowels > max_vowels:
                max_vowels = vowels
    
        return max_vowels