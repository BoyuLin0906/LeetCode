# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime 38 ms / Beats 98.74%
        Memory 16.6 MB / Beats 31.2%
        """
        odd_node = odd_head = ListNode(-1)
        even_node = even_head = ListNode(-1)
        # two list node
        while head and head.next:   
            odd_node.next = head
            odd_node = odd_node.next
            even_node.next = head.next
            even_node = even_node.next
            head = head.next.next
        # last one
        if head:
            odd_node.next = head 
            odd_node = odd_node.next
        # remove cycle
        even_node.next = None
        # combine
        odd_node.next = even_head.next
        return odd_head.next