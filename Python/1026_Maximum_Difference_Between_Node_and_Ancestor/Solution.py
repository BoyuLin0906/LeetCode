# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Runtime 34 ms / Beats 98.16%
        Memory 19.9 MB / Beats 60.26%
        """
        self.max_diff = 0

        def dfs(node, max_val=-1, min_val=inf):
            if not node: return
            
            if max_val != -1 and min_val != inf:
                self.max_diff = max(self.max_diff, abs(max_val-node.val), abs(min_val-node.val))
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)

            dfs(node.left, max_val, min_val)
            dfs(node.right, max_val, min_val)

        dfs(root)

        return self.max_diff