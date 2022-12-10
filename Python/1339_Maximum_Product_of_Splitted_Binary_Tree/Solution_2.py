# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Runtime 1069 ms / Beats 10.49%
        Memory 74.9 MB / Beats 77.58%
        """
        self.total_sum = 0
        self.max_product = 0

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.max_product = max(self.max_product, 
                                   (self.total_sum - left) * left,
                                   (self.total_sum - right) * right)
            return left + right + node.val

        self.total_sum = dfs(root)
        dfs(root)

        return self.max_product % (10**9 + 7)