# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder : mid -> left -> right
        # inorder : left -> mid -> right
        if not preorder: return None
        
        node = TreeNode(preorder[0])
        if len(preorder) == 1: return node
        
        inorder_idx = inorder.index(preorder[0])
        left_len = len(inorder[:inorder_idx])
        
        node.left = self.buildTree(preorder[1:left_len+1], inorder[:inorder_idx])
        node.right = self.buildTree(preorder[1+left_len:], inorder[inorder_idx+1:])
        
        return node