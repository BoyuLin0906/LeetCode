/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 54 ms / Beats 96.15%
Memory 7.14 MB / Beats 92.31%
*/
func doubleIt(head *ListNode) *ListNode {

    prev_node := &ListNode{Val: 0, Next: head}
    prev_head := prev_node
    curr_node := head

    for curr_node != nil {
        tmp_val := curr_node.Val * 2 
        if tmp_val < 10 {
            curr_node.Val = tmp_val
        } else {
            prev_node.Val++
            curr_node.Val = tmp_val % 10
        } 
        prev_node = curr_node
        curr_node = curr_node.Next
    }   

    if prev_head.Val != 0 {
        return prev_head 
    }
    return head
}