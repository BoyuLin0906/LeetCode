/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 334 ms / Beats 34.72%
Memory 15.17 MB / Beats 58.33%
*/

func mergeNodes(head *ListNode) *ListNode {
    
    dummy_node := &ListNode{Val:-1}
    nxt_node := dummy_node

    sum := 0
    first_flag := true
    for head != nil {
        if head.Val == 0 && !first_flag {
            nxt_node.Next = &ListNode{Val:sum}
            nxt_node = nxt_node.Next
            sum = 0
        } else {
            sum += head.Val
        }
        first_flag = false
        head = head.Next
    }
    
    return dummy_node.Next
}