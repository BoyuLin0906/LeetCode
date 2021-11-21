# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        value_mapping_index = {value: index for index, value in enumerate(inorder)}

        def helper(left, right):
            if left <= right:
                root_val = postorder.pop()
                node = TreeNode(root_val)
                
                mid_index = value_mapping_index[root_val]
                node.right = helper(mid_index+1, right)
                node.left = helper(left, mid_index-1)
                
                return node
        
        return  helper(0, len(inorder)-1)