from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional['TreeNode']) -> int:
        if root is None:
            return None
        current_level = deque((root,))
        best = root.val
        best_level = 1
        level = 0
        while current_level:
            next_level = deque()
            level += 1
            level_value = 0
            while current_level:
                node = current_level.pop()
                level_value += node.val
                for child in (node.left, node.right):
                    if child is not None:
                        next_level.append(child)
            if best < level_value:
                best = level_value
                best_level = level
            current_level = next_level
        return best_level