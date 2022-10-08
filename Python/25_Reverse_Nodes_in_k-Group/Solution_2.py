# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Runtime: 71 ms, faster than 71.96% of Python3 online submissions for Reverse Nodes in k-Group.
        Memory Usage: 15.2 MB, less than 40.67% of Python3 online submissions for Reverse Nodes in k-Group.
        """
        dummy_head = tmp_node = ListNode(-1)
        dummy_head.next = left_node = right_node = head 
        
        while True:
            count = 0
            
            while right_node and k > count:
                count += 1
                right_node = right_node.next
                
            if count == k:
                prev_node = right_node
                curr_node = left_node
                # reverse k-group 
                # 1. dummy - (a - b) - c
                # 2. dummy   (b - a) - c
                #      |          L    R
                #      +----------^      
                for _ in range(k):
                    curr_tmp_node = curr_node
                    curr_node = curr_node.next
                    curr_tmp_node.next = prev_node
                    prev_node = curr_tmp_node 
                # connect k-group
                # 3. dummy - (b - a) - c
                # 4. dummy - (b - a) - c
                #                 ^
                #              tmp_node
                # 5. dummy - (b - a) - c
                #                     L,R                    
                tmp_node.next = prev_node
                tmp_node = left_node
                left_node = right_node
            else:
                return dummy_head.next