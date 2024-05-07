/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 100 ms / Beats 15.38%
Memory 8.12 MB / Beats 30.77%
*/
func doubleIt(head *ListNode) *ListNode {

    dummy_node := head
    stack := make([]*ListNode, 0)

    for head != nil {
        stack = append(stack, head)
        head = head.Next
    }

    next_val := 0
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        tmp_val := node.Val * 2 + next_val
        if tmp_val / 10 == 1 {
            next_val = 1
        } else {
            next_val = 0
        }
        node.Val = tmp_val % 10
        stack = stack[:len(stack)-1]
    }

    if next_val == 1 {
        return &ListNode{Val: 1, Next: dummy_node}
    }

    return dummy_node
}