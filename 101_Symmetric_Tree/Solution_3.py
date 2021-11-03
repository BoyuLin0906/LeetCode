# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(root.left, root.right)]
        
        while stack:
            node_1, node_2 = stack.pop()
            if not node_1 and not node_2:
                continue
            elif not node_1 or not node_2:
                return False
            elif node_1.val != node_2.val:
                return False
            stack.append((node_1.left, node_2.right))
            stack.append((node_1.right, node_2.left))
        return True