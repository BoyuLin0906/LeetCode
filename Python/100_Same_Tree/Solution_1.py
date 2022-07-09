# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack_p = [p]
        stack_q = [q]
        
        while stack_p and stack_q:
            p_node = stack_p.pop()
            q_node = stack_q.pop()
            if bool(p_node) ^ bool(q_node):  return False
            if p_node and q_node and p_node.val != q_node.val: return False
            
            if p_node:
                stack_p.append(p_node.left)
                stack_p.append(p_node.right)
            if q_node:
                stack_q.append(q_node.left)
                stack_q.append(q_node.right)
            
        if len(stack_p) == 0 and len(stack_q) == 0:
            return True
        else:
            return False