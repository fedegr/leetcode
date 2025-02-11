from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional["TreeNode"]) -> int:
        stack = deque()
        stack.append((root, 1))

        max_depth = 0
        while len(stack) > 0:
            current, depth = stack.pop()

            if current is None:
                continue
            
            if depth > max_depth:
                max_depth = depth
            
            for child in (current.left, current.right):
                if child is not None:
                    stack.append((child, depth + 1))
        
        return max_depth

