class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        opening = 0
        closing = 0
        wildcard = 0

        for i in range(0, len(s)):
            if locked[i] == '0':
                wildcard += 1
            elif s[i] == '(':
                opening += 1
            else:
                closing += 1

            if wildcard < closing - opening:
                return False

        opening = 0
        closing = 0
        wildcard = 0

        for i in reversed(range(0, len(s))):
            if locked[i] == '0':
                wildcard += 1
            elif s[i] == '(':
                opening += 1
            else:
                closing += 1

            if wildcard < opening - closing:
                return False

        return True
                