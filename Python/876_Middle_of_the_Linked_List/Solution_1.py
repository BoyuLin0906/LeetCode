# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime 35 ms / Beats 87.26%
        Memory 13.8 MB / Beats 96.17%
        """
        slow_node = head
        head_idx = slow_idx = 0

        while head:
            if head_idx and (head_idx // 2) == slow_idx + 1:
                slow_node = slow_node.next
                slow_idx += 1

            head = head.next
            head_idx += 1

        if head_idx % 2 == 0:
            slow_node = slow_node.next

        return slow_node