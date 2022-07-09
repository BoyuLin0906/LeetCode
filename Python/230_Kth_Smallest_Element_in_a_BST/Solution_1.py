# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        node_val_list = list()
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                node_val_list.append(node.val)
        dfs(root)
        node_val_list.sort()
        return node_val_list[k-1]