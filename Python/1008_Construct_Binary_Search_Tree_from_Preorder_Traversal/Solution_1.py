# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        # insertion
        for val in preorder:
            self.createBST(root, val)
        return root
    
    def createBST(self, root, num):
        # recursive method
        if root is None:
            return TreeNode(num)
        else:
            if root.val == num:
                return root
            elif root.val < num:
                root.right = self.createBST(root.right, num)
            else:
                root.left = self.createBST(root.left, num)
        return root
        