# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Runtime: 61 ms, faster than 80.93% of Python3 online submissions for Reverse Nodes in k-Group.
        Memory Usage: 15.3 MB, less than 40.67% of Python3 online submissions for Reverse Nodes in k-Group.
        """
        # resursion
        def do_recursion(node):
            count = 0
            node_list = list()
            # collect nodes
            while node and count < k:
                node_list.append(node)
                node = node.next
                count += 1
            
            # still do recursion if amount is equal to k
            node_len = len(node_list)
            next_node = None
            if node:
                next_node = do_recursion(node)
            elif not node_list:
                return None
            elif node_len < k:
                return node_list[0]
            
            # reverse nodes
            for idx in range(1, node_len):
                node_list[idx].next = node_list[idx-1]
            node_list[0].next = next_node

            return node_list[node_len-1]

        return do_recursion(head)
