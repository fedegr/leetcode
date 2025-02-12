from typing import Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        stack = deque()
        stack.append((root, tuple()))
        while stack:
            node, path = stack.pop()
            if node is None:
                continue
                        
            path = (*path, node.val)
            path_sum = 0
            i = 0
            for i in range(len(path)):
                path_sum += path[-i-1]

                if path_sum == targetSum:
                    ans += 1
            
            for child in (node.left, node.right):
                stack.append((child, path))

        return ans