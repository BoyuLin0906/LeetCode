# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def insertTree(_nums):
            if _nums:
                length = len(_nums)
                mid = length // 2
                node = TreeNode(_nums[mid])
                node.left = insertTree(_nums[0:mid])
                node.right = insertTree(_nums[mid+1:length])
                return node
                
        node = insertTree(nums)
            
        return node