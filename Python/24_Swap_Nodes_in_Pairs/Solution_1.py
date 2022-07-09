# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        head = ListNode(-1, head)
        top = head

        while head and head.next and head.next.next:
            node_2 = head.next
            node_3 = head.next.next
            node_last =  head.next.next.next
            head.next = node_3
            node_3.next = node_2
            node_2.next = node_last
            head = node_2
              
        return top.next