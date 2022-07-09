# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.result = []
        self.BFS(root, x, y)
        
        node_1, node_2 = self.result[0], self.result[1]
        return node_1[0] != node_2[0] and node_1[1] == node_2[1]
    
    def BFS(self, node, x, y):
        # First in first out
        # first node
        queue = deque([(node, None, 0)])
        while queue or len(self.result) != 2:
            # pop item from left (head)
            node, parent, depth = queue.popleft()
            
            if node.val == x or node.val == y:
                self.result.append((parent, depth))
            # add in queue from right (tail)
            if node.left:
                queue.append((node.left, node, depth+1))
            if node.right:
                queue.append((node.right, node, depth+1))