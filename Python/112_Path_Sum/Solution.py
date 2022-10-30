# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Runtime: 81 ms, faster than 60.67% of Python3 online submissions for Path Sum.
        Memory Usage: 15 MB, less than 92.22% of Python3 online submissions for Path Sum.
        """
        # DFS
        if not root: return False
        tmp_sum = targetSum - root.val
        
        if tmp_sum == 0 and not root.left and not root.right: 
            return True
        
        left = self.hasPathSum(root.left, tmp_sum)
        right = self.hasPathSum(root.right, tmp_sum)
        
        return left or right