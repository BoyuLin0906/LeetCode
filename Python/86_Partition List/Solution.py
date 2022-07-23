# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = res_head = ListNode(-1)
        temp = head
        
        temp = temp_head = ListNode(-2)
        while head:
            if head.val < x:
                res.next = head
                res = res.next
            else:
                temp.next = head
                temp = temp.next
            head = head.next
            
        temp.next = None
        res.next = temp_head.next
        
        return res_head.next