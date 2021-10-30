# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        fast_runner = slow_runner = head
        
        while True:
            
            if not fast_runner.next or not fast_runner.next.next: 
                return False
            fast_runner = fast_runner.next.next
        
            if slow_runner == fast_runner:
                return True
            slow_runner = slow_runner.next