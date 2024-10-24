"""
Runtime : 0 ms, Beats 100.00%
Memory : 16.75 MB, Beats 16.61%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        no_swap = self.flipEquiv(root1.left, root2.left)
        no_swap = no_swap and self.flipEquiv(root1.right, root2.right)

        swap = self.flipEquiv(root1.left, root2.right)
        swap = swap and self.flipEquiv(root1.right, root2.left)

        return no_swap or swap