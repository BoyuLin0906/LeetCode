# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Runtime: 29 ms, faster than 97.07% of Python3 online submissions for Binary Tree Postorder Traversal.
        Memory Usage: 13.8 MB, less than 96.49% of Python3 online submissions for Binary Tree Postorder Traversal.
        """
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                res.append(node.val)
        
        return res[::-1]