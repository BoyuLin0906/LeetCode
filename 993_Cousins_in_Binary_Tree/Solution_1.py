# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_root = []
        y_root = []
        x_depth = self.find_node(root, root, x_root ,x, 0)
        y_depth = self.find_node(root, root, y_root ,y, 0)

        if x_depth != y_depth: 
            return False
        else:
            x_root = x_root.pop()
            y_root = y_root.pop()
            if x_root.val == y_root.val:
                return False
            else:
                return True
        
    def find_node(self, parent, root, root_record, val, depth):
        if root.val == val:
            root_record.append(parent)
            return depth
        
        depth = depth + 1
        left_val, right_val = 0, 0
        if root.left:
            left_val = self.find_node(root, root.left, root_record, val, depth)
        if root.right:
            right_val = self.find_node(root, root.right, root_record, val, depth)
        return max(left_val, right_val)