"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Runtime: 43 ms, faster than 98.13% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        Memory Usage: 15.3 MB, less than 48.93% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        """
        if not root: return root

        queue = deque([(root,0)])
        pre_node = None
        
        while queue:
            node, height = queue.popleft()
            
            if pre_node and pre_node[1] == height: 
                pre_node[0].next = node
            
            if node.left:
                queue.append((node.left, height+1))
                
            if node.right:
                queue.append((node.right, height+1))
            
            pre_node = (node, height)
        
        return root