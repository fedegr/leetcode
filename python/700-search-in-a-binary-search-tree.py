from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST_recursive(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        if root is None:
            return None
        
        if val < root.val:
            return self.searchBST_recursive(root.left, val)
        elif val > root.val:
            return self.searchBST_recursive(root.right, val)
        return root

    def searchBST(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        node = root
        while node is not None:
            if node.val == val:
                return node
        
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
        return None
