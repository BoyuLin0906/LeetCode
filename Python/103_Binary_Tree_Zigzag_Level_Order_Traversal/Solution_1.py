# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime 34 ms / Beats 66.77%
        Memory 14.1 MB / Beats 94%
        """
        if not root: return []

        queue = [(root, 0)]
        res_dict = collections.defaultdict(list)
        max_level = 0

        while queue:
            node, level = queue.pop(0)
            res_dict[level].append(node.val)
            max_level = level

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
            
        res = []
        for level in range(max_level+1):
            if level % 2 == 1:
                res_dict[level] = res_dict[level][::-1]
            res.append(res_dict[level])
        
        return res