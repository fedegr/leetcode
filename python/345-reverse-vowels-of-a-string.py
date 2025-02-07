class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ('a', 'e', 'i', 'o', 'u')
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].lower() not in vowels:
                start += 1
            elif s[end].lower() not in vowels:
                end -= 1
            else:
                swap = s[start]
                s[start] = s[end]
                s[end] = swap
                start += 1
                end -= 1
        return ''.join(s)
