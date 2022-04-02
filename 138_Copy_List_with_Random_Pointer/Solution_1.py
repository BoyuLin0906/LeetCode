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
        temp_head = head
        node_list = []
        result = result_head = Node(-1)
        
        # add in node list
        while temp_head:
            count_head = head
            count = None      
            if temp_head.random != None:
                count = 0
                while count_head:
                    if temp_head.random == count_head: break
                    count += 1
                    count_head = count_head.next
            node_list.append((Node(temp_head.val), count))
            temp_head = temp_head.next
        
        # establish relation
        for node_index in range(len(node_list)):
            node, random_index = node_list[node_index]
            result.next = node
            if random_index != None:
                inter_node, _ = node_list[random_index]
                node.random = inter_node
            result = result.next
                    
        return result_head.next