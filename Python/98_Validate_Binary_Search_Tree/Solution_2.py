# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 41ms, Beats 91.32%
        Memory : 18.76MB, Beats 65.08%
        """
        def validate(node, left_val, right_val):
            if not node:
                return True
            if not (left_val < node.val < right_val):
                return False
            
            left_valid = validate(node.left, left_val, node.val)
            right_valid =  validate(node.right, node.val, right_val)
            return left_valid and right_valid

        return validate(root, float(-inf), float(inf))