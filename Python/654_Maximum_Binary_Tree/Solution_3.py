# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        
        if not nums: return None
            
        max_idx = nums.index(max(nums))
    
        return TreeNode(nums[max_idx], self.constructMaximumBinaryTree(nums[0:max_idx]), self.constructMaximumBinaryTree(nums[max_idx+1:]))