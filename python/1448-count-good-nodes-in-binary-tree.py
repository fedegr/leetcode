from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: "TreeNode") -> int:
        stack = deque()
        stack.append((root, root.val))

        good_count = 0
        while len(stack) > 0:
            current, max_in_path = stack.pop()

            if max_in_path <= current.val:
                max_in_path = current.val
                good_count += 1
                
            for child in (current.left, current.right):
                if child is not None:
                    stack.append((child, max_in_path))
        
        return good_count
