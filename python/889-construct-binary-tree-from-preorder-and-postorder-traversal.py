from typing import List, Optional
from tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def construct_from_pre_post(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    
    if len(preorder) == 0:
        return None
    
    node = TreeNode(preorder[0])
    
    if len(preorder) > 1:
        left_val = preorder[1]
        right_val = postorder[-2]

        if left_val == right_val:
            node.right = construct_from_pre_post(
                preorder[1:],
                postorder[:-1],
            )
        else:
            pre_order_right_node_position = preorder.index(right_val, 1)
            post_order_left_node_position = postorder.index(left_val)

            node.left = construct_from_pre_post(
                preorder[1:pre_order_right_node_position],
                postorder[0:post_order_left_node_position+1],
            )

            node.right = construct_from_pre_post(
                preorder[pre_order_right_node_position:],
                postorder[post_order_left_node_position+1:-1],
            )

    return node


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return construct_from_pre_post(preorder, postorder)