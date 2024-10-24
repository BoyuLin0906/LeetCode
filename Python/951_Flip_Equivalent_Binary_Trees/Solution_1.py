"""
Runtime : 0 ms, Beats 100.00%
Memory : 16.60 MB, Beats 57.29%
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        dummy = TreeNode(-1)

        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        queue_1 = [(dummy, root1)]
        queue_2 = [(dummy, root2)]
  
        while queue_1 and queue_2:

            queue_1_len = len(queue_1)
            queue_2_len = len(queue_2)
            if queue_1_len != queue_2_len:
                return False

            checked = dict()
            for _ in range(queue_1_len):
                parent, node = queue_1.pop(0)
                print()
                if parent.val not in checked:
                    checked[parent.val] = set()
                checked[parent.val].add(node.val)

                if node.left:
                    queue_1.append((node, node.left))
                if node.right:
                    queue_1.append((node, node.right))

            for _ in range(queue_2_len):
                parent, node = queue_2.pop(0)
                
                if not parent.val in checked:
                    return False

                if not node.val in checked[parent.val]:
                    return False

                if node.left:
                    queue_2.append((node, node.left))
                if node.right:
                    queue_2.append((node, node.right))

        if len(queue_1) != 0 or len(queue_2) != 0:
            return False
        return True