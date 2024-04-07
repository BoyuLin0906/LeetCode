/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 0 ms / Beats 100.00%
Memory 2.34 MB / Beats 17.26%
*/

// one pass
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    res := &ListNode{Val: -1, Next: head}
    curr_node, prev_node := res, res

    for curr_node != nil {
        if n < 0 {
            prev_node = prev_node.Next
        }
        curr_node = curr_node.Next
        n--
    }

    if prev_node.Next != nil {
        prev_node.Next = prev_node.Next.Next
    }

    return res.Next
}