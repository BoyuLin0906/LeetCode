# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Runtime 23 ms / Beats 99.68%
        Memory 13.8 MB / Beats 89.69%
        """
        root1_vals = []
        root2_vals = []

        def dfs(node, val_list):
            if not node: 
                return None
            elif node.left or node.right:
                dfs(node.left, val_list)
                dfs(node.right, val_list)
            else:
                val_list.append(node.val)

        dfs(root1, root1_vals)
        dfs(root2, root2_vals)

        return root1_vals == root2_vals