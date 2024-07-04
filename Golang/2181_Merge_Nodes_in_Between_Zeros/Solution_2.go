/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 298 ms / Beats 66.67%
Memory 18.25 MB / Beats 27.78%
*/
func mergeNodes(head *ListNode) *ListNode {
    
    curr_node := head.Next
    prev_node := head

    for curr_node.Next != nil {
        if curr_node.Val == 0 {
            prev_node.Next = curr_node
            prev_node = curr_node
        }
        prev_node.Val += curr_node.Val
        curr_node = curr_node.Next
    }
    prev_node.Next = nil
    
    return head
}