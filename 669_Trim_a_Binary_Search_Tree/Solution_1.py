# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        self.result = TreeNode(-1)
        def dfs(node):
            if node:
                if node.val >= low and node.val <= high: 
                    build(self.result, node)
                dfs(node.left)
                dfs(node.right)
        
        def build(temp, node):
            if node.val < temp.val:
                if temp.left:
                    build(temp.left, node)
                else:
                    temp.left = TreeNode(val=node.val)
            else:
                if temp.right:
                    build(temp.right, node)
                else:
                    temp.right = TreeNode(val=node.val)
        dfs(root)
        return self.result.right