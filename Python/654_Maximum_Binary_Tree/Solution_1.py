# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(root_node, nums_list, direction):
            if not nums_list: return None
            
            max_value_idx = nums_list.index(max(nums_list))
            cur_node = TreeNode(nums_list[max_value_idx])
            
            if direction == 'left': root_node.left = cur_node
            else: root_node.right = cur_node
            
            build_tree(cur_node, nums_list[:max_value_idx], 'left')
            build_tree(cur_node, nums_list[max_value_idx+1:], 'right')
            
        head_node = TreeNode(-1)
        build_tree(head_node, nums, 'left')
        
        return head_node.left