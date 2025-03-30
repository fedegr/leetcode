from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """ Return a partition of the given string into as many parts as possible 
        so that each letter appears in at most one part.

        >>> Solution().partitionLabels("abc")
        [1, 1, 1]
        >>> Solution().partitionLabels("abcdcbaeefffghg")
        [7, 2, 3, 3]
        >>> Solution().partitionLabels("aabab")
        [5]
        """


        last_occurrence = dict()
        for i, c in enumerate(s):
            last_occurrence[c] = i

        groups = []
        group_start = 0
        group_end = 0
        for i, c in enumerate(s):
            if last_occurrence[c] == group_end and i == group_end:
                groups.append(group_end - group_start + 1)
                group_start = group_end + 1
                group_end = group_start
            elif last_occurrence[c] > group_end:
                group_end = last_occurrence[c]
        
        return groups


if __name__ == "__main__":
    import doctest
    doctest.testmod()
