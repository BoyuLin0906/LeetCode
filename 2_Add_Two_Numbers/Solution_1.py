# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum = ListNode()
        head = sum
        carry = 0
        
        def do_carry(val):
            _carry = 0
            if (val // 10) > 0:
                _carry = 1
                val -= 10 
            return _carry, val
            
        while l1 or l2:
            if l1 and l2:
                carry, sum.val = do_carry(l1.val + l2.val + carry)
            elif l1 and l2 is None:
                carry, sum.val = do_carry(l1.val + carry)
            elif l1 is None and l2:
                carry, sum.val = do_carry(l2.val + carry)
   
            if (l1 and l1.next) or (l2 and l2.next):
                sum.next = ListNode()
                sum = sum.next
            elif carry > 0:
                sum.next = ListNode(1)
                
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return head