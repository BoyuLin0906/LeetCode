/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 231 ms / Beats 41.27%
Memory 13.33 MB / Beats 60.32%
*/
func removeNodes(head *ListNode) *ListNode {
    
   if head.Next == nil {
        return head
    }

    next_node := removeNodes(head.Next)
    if next_node.Val > head.Val {
        return next_node
    }

    head.Next = next_node
    return head
}