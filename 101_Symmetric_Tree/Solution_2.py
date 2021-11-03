# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checking(left_node, right_node):
            
            if left_node and right_node and left_node.val == right_node.val:
                return checking(left_node.left, right_node.right) and checking(left_node.right, right_node.left)
            elif left_node == right_node:
                return True
            return False
        
        return checking(root.left, root.right)