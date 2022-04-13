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
        root = TreeNode(None)
        stack = [(root, preorder, inorder, "left")]
        
        while stack:
            parent, sub_preorder, sub_inorder, direction = stack.pop() 
            node = TreeNode(sub_preorder[0])
            
            if direction == "left": parent.left = node
            else: parent.right = node
                
            inorder_idx = sub_inorder.index(sub_preorder[0])
            sub_inorder_len = len(sub_inorder)
            left_len = len(sub_inorder[:inorder_idx])
            
            if sub_inorder[inorder_idx+1:]:
                stack.append((node, sub_preorder[1+left_len:], sub_inorder[inorder_idx+1:], "right"))
            if sub_inorder[:inorder_idx]:
                stack.append((node, sub_preorder[1:left_len+1], sub_inorder[:inorder_idx], "left"))

        return root.left