# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        node = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])

        left_len = len(inorder[0:index])
        right_len = len(inorder[index+1:len(inorder)])
        
        if left_len:
            node.left = self.buildTree(inorder[0:index], postorder[0:left_len])
        if right_len:
            node.right = self.buildTree(inorder[index+1:len(inorder)], postorder[left_len: left_len+right_len])
        return node