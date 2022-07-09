# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseList(head, prev):
            if not head: return prev
            next_node = head.next
            head.next = prev
            return reverseList(next_node, head)
        
        return reverseList(head, None)