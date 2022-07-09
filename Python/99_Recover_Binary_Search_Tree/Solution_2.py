# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev_node = x_node = y_node = None
        
        def dfs(node):
            if not node: return
            nonlocal prev_node, x_node, y_node
            
            dfs(node.left)
        
            if prev_node and node.val < prev_node.val:
                y_node = node
                if not x_node: x_node = prev_node
                else: return     
            prev_node = node
            
            dfs(node.right)
            
        dfs(root)
        x_node.val, y_node.val = y_node.val, x_node.val