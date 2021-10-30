# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iteration
        stack, result = [], []
        
        while stack or root:
            while root:
                # save all nodes
                stack.append(root)
                # find all left child node
                root = root.left
            
            # pop node
            root = stack.pop()
            result.append(root.val)
            
            # find right child node
            root = root.right
            
        return result