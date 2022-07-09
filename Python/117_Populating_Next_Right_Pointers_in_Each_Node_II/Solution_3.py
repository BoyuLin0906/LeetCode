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
        Runtime: 59 ms, faster than 63.82% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        Memory Usage: 15.3 MB, less than 92.97% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
        """
        if not root: return root

        current_node = head_node = root
        temp_node = Node(-101)
        
        while head_node:
            # iterate for height
            current_node = head_node # from most left mode
            prev_node = temp_node
            
            while current_node:
                # iterate for width
                if current_node.left:
                    prev_node.next = current_node.left
                    prev_node = prev_node.next

                if current_node.right:
                    prev_node.next = current_node.right
                    prev_node = prev_node.next
                    
                current_node = current_node.next
            
            head_node = temp_node.next # next level of height
            temp_node.next = None # reset
        
        return root