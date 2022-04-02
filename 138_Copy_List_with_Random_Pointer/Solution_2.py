"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_table, pre_node, node = dict(), None, head
        
        while node:
            if node not in node_table:
                node_table[node] = Node(node.val)
            
            # connect next node
            if pre_node: pre_node.next = node_table[node]
            else: head = node_table[node]
                
            if node.random:
                if node.random not in node_table:
                    node_table[node.random] = Node(node.random.val)
                # connect random node
                node_table[node].random = node_table[node.random]
                
            # next one
            pre_node, node = node_table[node], node.next
            
        return head