# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root.left, root.right)]
        sum = 0
        
        while stack:
            left_node, right_node = stack.pop()
            
            if left_node and not left_node.left and not left_node.right:
                sum += left_node.val
                
            if left_node:
                stack.append((left_node.left, left_node.right))
            if right_node:
                stack.append((right_node.left, right_node.right))
                
        return sum