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
        
        value_mapping_index = {value: index for index, value in enumerate(inorder)}
        preorder = preorder[::-1]
        
        def helper(left, right):
            if left <= right:
                root_val = preorder.pop()
                node = TreeNode(root_val)
                
                mid_index = value_mapping_index[root_val]
                node.left = helper(left, mid_index-1)
                node.right = helper(mid_index+1, right)
                return node
        
        return  helper(0, len(inorder)-1)