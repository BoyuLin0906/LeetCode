"""
Runtime 287 ms / Beats 94.06%
Memory 57.35 MB / Beats 82.17%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(-1) 
        queue = [(dummy, root)]
        res= []

        while queue:

            queue_len = len(queue)
            parent_to_cousin_sum = dict()
            totol = 0
            for idx in range(queue_len):
                parent, node = queue[idx]
                if not parent in parent_to_cousin_sum:
                    parent_to_cousin_sum[parent] = 0
                   
                parent_to_cousin_sum[parent] -= node.val
                totol += node.val        

            for _ in range(queue_len):
                parent, node = queue.pop(0)
                node.val = parent_to_cousin_sum[parent] + totol

                if node.left:
                    queue.append((node, node.left))
                if node.right:
                    queue.append((node, node.right))

        return root