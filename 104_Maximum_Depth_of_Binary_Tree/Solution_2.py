# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        stack = [root]
        node_nums = 1
        level = 0
        while stack:
            node = stack.pop(0)
            
            if node.left: stack.append(node.left)     
            if node.right: stack.append(node.right)
                
            node_nums -= 1
            if node_nums == 0:
                level += 1
                node_nums = len(stack)
        
        return level