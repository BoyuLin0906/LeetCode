# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
		Runtime: 75 ms, faster than 77.90% of Python3 online submissions for Balanced Binary Tree.
		Memory Usage: 18.5 MB, less than 90.47% of Python3 online submissions for Balanced Binary Tree.
        """
        # DFS
        def helper(node):
            if not node: return 1
            
            left = helper(node.left) 
            right = helper(node.right)
            
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return helper(root) != -1