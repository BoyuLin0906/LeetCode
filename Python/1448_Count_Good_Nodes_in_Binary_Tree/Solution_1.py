"""
Runtime 123 ms / Beats 81.15%
Memory 31.14 MB / Beats 43.81%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -10**4-1)
        
    def dfs(self, node, max_num):
        if not node:
            return 0
        
        count = 0
        next_max_num = max(max_num, node.val)
        count += self.dfs(node.left, next_max_num)
        count += self.dfs(node.right, next_max_num)

        if node.val >= max_num:
            count += 1
        
        return count
