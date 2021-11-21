# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(None)
        stack = [(root, inorder, postorder, "left")]
        
        while stack:
            parent, sub_inorder, sub_postorder, ort = stack.pop() 
            node = TreeNode(sub_postorder[-1])
            if ort == "left":
                parent.left = node
            else:
                parent.right = node
            index = sub_inorder.index(sub_postorder[-1])
            sub_inorder_len = len(sub_inorder)
            left_len = len(sub_inorder[0:index])
            right_len = len(sub_inorder[index+1:sub_inorder_len])
            
            if sub_inorder[index+1:sub_inorder_len]:
                stack.append((node, sub_inorder[index+1:sub_inorder_len], sub_postorder[left_len: left_len+right_len], "right"))
            if sub_inorder[0:index]:
                stack.append((node, sub_inorder[0:index], sub_postorder[0:left_len], "left"))

        return root.left