# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        _list = result = ListNode()
        while stack:
            node = stack.pop()
            _list.next = node
            _list = _list.next
        _list.next = None    
            
        return result.next