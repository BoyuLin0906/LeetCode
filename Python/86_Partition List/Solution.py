# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Runtime: 47 ms, faster than 67.21% of Python3 online submissions for Partition List.
        Memory Usage: 13.8 MB, less than 75.71% of Python3 online submissions for Partition List.
        """
        # linked list
        """
        [1]
        org: 1,4,3,2,5,2
        res: -1
        temp: -2
        
        [2]
        res: -1, 1, 2, 2
        temp: -2, 4, 3, 5
        
        [3]
        res: -1, 1, 2, 2, (4, 3, 5)
                              ^
                              |
        temp -2, (4, 3, 5) ---+
        """
        res = res_head = ListNode(-1)  
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