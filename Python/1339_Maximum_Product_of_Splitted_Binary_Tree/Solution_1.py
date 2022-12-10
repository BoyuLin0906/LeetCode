# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Runtime 356 ms / Beats 89.19%
        Memory 75.6 MB / Beats 38.79%
        """
        self.total_sum = 0
        self.sub_sum_list = []

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)

            self.total_sum += node.val
            self.sub_sum_list.append(right + left + node.val)
            return left + right + node.val

        dfs(root)
        max_product = 0
        for sub_sum in self.sub_sum_list:
            max_product = max(max_product, (self.total_sum - sub_sum) * sub_sum)

        return max_product % (10**9 + 7)