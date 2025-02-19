from typing import Dict, Tuple


class Solution:
    def _calculateHappyStrings(self, n: int, happyStringsCache: Dict[int, Tuple[str]]) -> Tuple[str]:
        if n not in happyStringsCache:
            smaller = self._calculateHappyStrings(n-1,happyStringsCache)
            happyStringsCache[n] = tuple(
                c + s
                for c in happyStringsCache[1]
                for s in smaller
                if c != s[0]
            )
        return happyStringsCache[n]

    def getHappyString(self, n: int, k: int) -> str:
        happyStringsCache = {1: ('a', 'b', 'c')}
        self._calculateHappyStrings(n, happyStringsCache)
        strings = happyStringsCache[n]
        if k <= len(strings):
            return strings[k-1]
        return ""
