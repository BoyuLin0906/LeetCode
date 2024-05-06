/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 195 ms / Beats 74.60%
Memory 13.08 MB / Beats 65.08%
*/
func removeNodes(head *ListNode) *ListNode {
    
    stack := make([]*ListNode, 0)
    for head != nil {
        for len(stack) > 0 && head.Val > stack[len(stack)-1].Val {
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, head)
        head = head.Next
    }

    for i := 0; i < len(stack)-1; i++ {
        stack[i].Next = stack[i+1]
    }

    return stack[0]
}