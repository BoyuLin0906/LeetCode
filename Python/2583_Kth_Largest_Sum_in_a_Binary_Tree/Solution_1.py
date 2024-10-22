"""
Runtime 266 ms / Beats 65.05%
Memory 53.04 MB / Beats 15.83%
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

        current_sum = 0
        next_queue = []
        level_sums = []
        while queue:
            node = queue.pop(0)
            current_sum += node.val

            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

            if not queue:
                queue = next_queue
                next_queue = []
                heapq.heappush(level_sums, -current_sum)
                current_sum = 0

        if len(level_sums) < k:
            return -1
            
        res = 0
        for _ in range(k):
            res = heapq.heappop(level_sums)
        res = -res

        return res