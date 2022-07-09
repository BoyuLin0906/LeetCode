# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.max_depth(root)
        return self.diameter
    
    def max_depth(self, root):
        if not root: return 0
        
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        
        self.diameter = max(left+right, self.diameter)
        return max(left, right) + 1