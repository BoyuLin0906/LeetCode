# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        tempA = headA
        while tempA:
            tempA.val *= -1
            tempA = tempA.next
        
        while headB:
            if headB.val < 0:
                break
            headB = headB.next
        
        while headA:
            headA.val *= -1
            headA = headA.next
        
        return headB