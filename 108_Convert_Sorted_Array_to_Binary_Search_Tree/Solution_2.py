# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def insertTree(left, right):
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(nums[mid])
                node.left = insertTree(left, mid-1)
                node.right = insertTree(mid+1, right)
                return node
                
        node = insertTree(0, len(nums)-1)
            
        return node