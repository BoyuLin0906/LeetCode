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
        # Morris Traversal
        curr_node = root
        prev_node, x_node, y_node = None, None, None
        
        while curr_node:
            if curr_node.left:
                temp = curr_node.left
                while temp.right and temp.right != curr_node: temp = temp.right
                if not temp.right:
                    temp.right = curr_node
                    curr_node = curr_node.left
                    continue
                else:
                    temp.right = None 
            
            if prev_node and curr_node.val < prev_node.val:
                print(curr_node.val, prev_node.val)
                if not x_node: x_node = prev_node
                y_node = curr_node
                
            prev_node = curr_node
            curr_node = curr_node.right
            
        x_node.val, y_node.val = y_node.val, x_node.val
            
                
        