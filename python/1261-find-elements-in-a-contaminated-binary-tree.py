from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional['TreeNode']):
        self.root = root    

    def find(self, target: int) -> bool:
        level = (target + 1).bit_length() - 1
        level_nodes = 2**level
        position = (target + 1 - level_nodes)

        node = self.root
        while level > 0 and node is not None:
            level -= 1
            level_nodes //= 2 
            if position >= level_nodes:
                position -= level_nodes
                node = node.right
            else:
                node = node.left
        
        return node is not None
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
