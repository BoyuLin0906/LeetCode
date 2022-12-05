# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	"""
		Runtime 24 ms / Beats 99.22%
		Memory 13.9 MB / Beats 55.96%
    	"""
        slow_node = head

        while head and head.next:
            slow_node = slow_node.next
            head = head.next.next
           
        return slow_node