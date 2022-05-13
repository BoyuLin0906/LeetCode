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
        Runtime: 55 ms, faster than 74.04% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        Memory Usage: 15.8 MB, less than 11.90% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        """
        if not root: return root
        results = [(root,0)]
        queue = deque(results)
        
        while queue:
            node, height = queue.popleft()
            
            if node.left:
                queue.append((node.left, height+1))
                results.append((node.left, height+1))
                
            if node.right:
                queue.append((node.right, height+1))
                results.append((node.right, height+1))
        
        for idx in range(len(results)-1):
            if results[idx][1] == results[idx+1][1]: 
                results[idx][0].next = results[idx+1][0]
        
        return root