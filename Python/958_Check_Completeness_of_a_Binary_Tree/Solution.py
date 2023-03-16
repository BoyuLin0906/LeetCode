# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    	"""
		Runtime 31 ms / Beats 91.14%
		Memory 13.9 MB / Beats 61.50%
    	"""
    	# BFS
        queue = [root]

        while queue[0]:
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)

        return not any(queue)