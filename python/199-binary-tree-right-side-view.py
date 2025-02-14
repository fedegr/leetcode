from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional["TreeNode"]) -> List[int]:
        queue = deque()
        queue.append((0,root))
        answer = []
        while queue:
            level, node = queue.popleft()
            if node is None:
                continue
            if level == len(answer):
                answer.append(node.val)
            
            for child in (node.right, node.left):
                queue.append((level + 1, child))
        
        return answer
