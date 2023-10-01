# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        inorder 

        Runtime : 43 ms, Beats 85.91%
        Memory : 19.1 MB, Beats 25.24%
        """ 
        prev_val = float("-inf")

        def validate(node):
            nonlocal prev_val
            if not node:
                return True

            status = validate(node.left)
            if not (status and prev_val < node.val):
                return False
            
            prev_val = node.val
            return validate(node.right)

        return validate(root)