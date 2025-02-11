from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional["TreeNode"], root2: Optional["TreeNode"]) -> bool:
        return self.leaves(root1) == self.leaves(root2)

    def leaves(self, root: Optional["TreeNode"]) -> bool:
        stack = deque()
        stack.append(root)

        children = []
        while len(stack) > 0:
            current = stack.pop()

            if current is None:
                continue

            if current.left is None and current.right is None:
                children.append(current.val)
            else:
                for child in (current.left, current.right):
                    if child is not None:
                        stack.append(child)
        
        return tuple(children)
    