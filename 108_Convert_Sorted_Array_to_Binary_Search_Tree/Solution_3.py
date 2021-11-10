# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(10**4 + 1) 
        queue = [(root, 0, len(nums) - 1, 0)]
        
        while queue:
            parent_node, left, right, left_flag =  queue.pop()
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(nums[mid])
                
                if left_flag == 0:
                    parent_node.left = node
                else:
                    parent_node.right = node
                # left
                queue.append((node, left, mid-1, 0))
                # right
                queue.append((node, mid+1, right, 1))
                
        return root.left