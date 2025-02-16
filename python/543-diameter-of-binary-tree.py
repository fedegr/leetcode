from typing import Optional, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameter_of_binary_tree(root: Optional['TreeNode']) -> Tuple[int, int]:
    if root is None:
        return (0, -1)
    dl, hl = diameter_of_binary_tree(root.left)
    dr, hr = diameter_of_binary_tree(root.right)
    return (max((dr, dl, hl + hr + 2)), max(hl, hr) + 1)

class Solution:
    def diameterOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        return diameter_of_binary_tree(root)[0]
