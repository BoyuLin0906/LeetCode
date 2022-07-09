# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")
            
        def find_max_path(node):
            if not node: return 0
            
            left_max = max(0, find_max_path(node.left))
            right_max = max(0, find_max_path(node.right))
            
            self.max_path = max(self.max_path, left_max + right_max + node.val)
            return max(left_max, right_max) + node.val
        
        find_max_path(root)
    
        return self.max_path