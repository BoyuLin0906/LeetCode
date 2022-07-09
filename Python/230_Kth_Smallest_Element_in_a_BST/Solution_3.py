# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Morris Traversal
        curr_node = root
        
        while curr_node:
            if not curr_node.left:
                # find the most left node (from smallest value)
                k -= 1
                if k == 0: return curr_node.val
                curr_node = curr_node.right
            else:
                next_node = curr_node.left
                
                # find most right node
                while next_node.right: next_node = next_node.right
                    
                # link current node to right leaf
                next_node.right = curr_node
                
                # change current node to left node and cancel the left link on current node
                temp_node = curr_node
                curr_node = curr_node.left
                temp_node.left = None
                
        return -1