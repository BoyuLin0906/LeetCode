# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def getSum(node, direct):
            if not node:
                return 0
            if not node.left and not node.right and direct == "l":
                return node.val
            return getSum(node.left, "l") + getSum(node.right, "r")
        
        return getSum(root.left, "l") + getSum(root.right, "r")