# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime 30 ms / Beats 87.39%
        Memory 14.1 MB / Beats 47.10%
        """
        if not root: return []

        queue = collections.deque([root])
        res = []
        if_even_level = False

        while queue:
            queue_len = len(queue)
            level_res = []

            for idx in range(queue_len):
                if if_even_level:
                    node = queue.pop()
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                # add all values in current level
                level_res.append(node.val)
            # add all levels in result
            res.append(level_res)
            # change status
            if_even_level = not if_even_level

        return res