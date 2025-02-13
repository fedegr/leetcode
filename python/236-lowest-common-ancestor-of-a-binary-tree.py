from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = {p.val: None, q.val: None}
        found = 0
        stack = deque()
        stack.append((root,tuple()))
        while stack:
            current, path = stack.pop()
            if current is None:
                continue
            
            path = (*path, current)
            if current.val in paths:
                paths[current.val] = path
                found += 1
            if found == 2:
                break
            
            for child in (current.left, current.right):
                stack.append((child, path))
        
        if found != 2:
            return None

        path_p = paths[p.val]
        path_q = paths[q.val]
        i = 0
        max_i = min(len(path_p), len(path_q))
        while i < max_i and path_p[i] == path_q[i]:
            i += 1
        
        return path_p[i - 1]
            