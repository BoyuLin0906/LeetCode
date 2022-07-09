# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        len_A = 0
        len_B = 0
        temp_a = headA
        temp_b = headB
        while temp_a:
            len_A += 1
            temp_a = temp_a.next
        
        while temp_b:
            len_B += 1
            temp_b = temp_b.next
            
        diff = len_A - len_B
        if diff > 0:
            while diff > 0:
                headA = headA.next
                diff-=1
        else:
             while diff < 0:
                headB = headB.next
                diff+=1
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None