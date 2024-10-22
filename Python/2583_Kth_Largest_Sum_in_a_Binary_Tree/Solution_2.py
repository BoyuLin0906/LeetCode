"""
Runtime 507 ms / Beats 17.56%
Memory 52.92 MB / Beats 15.99%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root]

        level_sums = []
        while queue:

            current_sum = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                current_sum += node.val
                
                if not node.left is None:
                    queue.append(node.left)
                if not node.right is None:
                    queue.append(node.right)
  
            heapq.heappush(level_sums, current_sum)
            if len(level_sums) > k:
                heapq.heappop(level_sums)

        if len(level_sums) < k:
            return -1

        res = level_sums[0]
        return res