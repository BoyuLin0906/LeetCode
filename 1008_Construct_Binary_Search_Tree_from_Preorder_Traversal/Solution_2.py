# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        for i in range(1, len(preorder)):
            current_root = root
            while True:
                if current_root.val > preorder[i]:
                    if current_root.left:
                        current_root = current_root.left
                    else:
                        current_root.left = TreeNode(preorder[i])
                        break
                else:
                    if current_root.right:
                        current_root = current_root.right
                    else:
                        current_root.right = TreeNode(preorder[i])
                        break
        return root