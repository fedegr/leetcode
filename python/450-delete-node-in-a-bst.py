from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional['TreeNode'], key: int) -> Optional['TreeNode']:
        prev = None
        current = root
        while current is not None and current.val != key:
            if key == current.val:
                break
            prev = current
            if key < current.val:
                current = current.left
            elif key > current.val:
                current = current.right
            
        
        if current is None:
            return root

        if current.left is not None:
            current.val = self.remove_biggest(current.left, current)
        elif current.right is not None:
            current.val = self.remove_smallest(current.right, current)
        elif prev is not None:
            if prev.left == current:
                prev.left = None
            elif prev.right == current:
                prev.right = None
        else:
            return None
        
        return root
        
    def remove_biggest(self, node, parent):
        prev = None
        while node.right is not None:
            prev = node
            node = node.right
        if prev is None:
            parent.left = node.left
        else:
            prev.right = node.left
        return node.val
    
    def remove_smallest(self, node, parent):
        prev = None
        while node.left is not None:
            prev = node
            node = node.left
        if prev is None:
            parent.right = node.right
        else:
            prev.left = node.right
        return node.val
