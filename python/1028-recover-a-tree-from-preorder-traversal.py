from typing import Optional
from collections import deque

from tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if len(traversal) == 0:
            return None
        
        i = 0
        path = deque()
        while i < len(traversal):
            dashes = 0
            while traversal[i] == '-':
                i += 1
                dashes += 1

            j = i
            while j < len(traversal) and traversal[j] != '-':
                j += 1
            
            node = TreeNode(int(traversal[i:j]))
            i = j
            while dashes != len(path):
                path.pop()
            
            if len(path) != 0:
                if path[-1].left is None:
                    path[-1].left = node
                else:
                    path[-1].right = node
            path.append(node)
        
        return path[0]

