# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        head_node = TreeNode(-1)
        nums_queue = [(head_node, nums, 'left')]
        
        while nums_queue:
            pre_node, cur_nums, direction = nums_queue.pop()
            if cur_nums:
                max_value_idx = cur_nums.index(max(cur_nums))
                cur_node = TreeNode(cur_nums[max_value_idx])

                if direction == 'left': pre_node.left = cur_node
                else: pre_node.right = cur_node

                nums_queue.append((cur_node, cur_nums[max_value_idx+1:], 'right'))
                nums_queue.append((cur_node, cur_nums[:max_value_idx], 'left'))

        return head_node.left