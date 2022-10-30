# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 651 ms, faster than 85.39% of Python3 online submissions for Minimum Depth of Binary Tree.
        Memory Usage: 54.6 MB, less than 52.99% of Python3 online submissions for Minimum Depth of Binary Tree.
        """
        # DFS
        if not root: return 0
        self.min_depth = inf
        
        def helper(node, depth):
            if not node: return False
            
            left = helper(node.left, depth+1)
            right = helper(node.right, depth+1)
            
            if not left and not right:
                self.min_depth = min(self.min_depth, depth)
            return True

        helper(root, 1)
        
        return self.min_depth