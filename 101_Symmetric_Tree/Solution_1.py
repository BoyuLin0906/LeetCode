# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left_stack = [root.left]
        right_stack = [root.right]
        
        while left_stack and right_stack:
            left_node = left_stack.pop()
            right_node = right_stack.pop()
            
            if left_node and right_node and left_node.val != right_node.val: return False
            elif bool(left_node) ^ bool(right_node): return False
            
            if left_node:
                left_stack.append(left_node.left)
                left_stack.append(left_node.right)
            if right_node:                  
                right_stack.append(right_node.right)
                right_stack.append(right_node.left)
            
            
        if len(left_stack) != 0 or len(right_stack) != 0: return False
        else: return True