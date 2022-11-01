# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
		Runtime: 48 ms, faster than 71.45% of Python3 online submissions for Binary Tree Postorder Traversal.
		Memory Usage: 13.8 MB, less than 60.61% of Python3 online submissions for Binary Tree Postorder Traversal.
        """
        # DFS
        if not root: return [] 
        
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        
        return left + right + [root.val]