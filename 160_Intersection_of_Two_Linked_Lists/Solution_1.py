# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        tempA, tempB = headA, headB
        
        while tempA != tempB:
            
            if tempA:
                tempA = tempA.next
            else:
                tempA = headB
                
            if tempB:
                tempB = tempB.next
            else:
                tempB = headA
                
        return tempA