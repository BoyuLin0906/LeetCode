# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.result = []
        self.DFS(root, None, 0 ,x, y)
        # get two nodes
        node_1, node_2 = self.result
        # compare
        return node_1[0] != node_2[0] and node_1[1] == node_2[1]
        
    def DFS(self, node, parent, depth, x, y):
        if not node:
            return None
        
        if node.val == x or node.val == y:
            self.result.append((parent, depth))
        # left
        self.DFS(node.left, node, depth+1, x, y)
        # right
        self.DFS(node.right, node, depth+1, x, y)