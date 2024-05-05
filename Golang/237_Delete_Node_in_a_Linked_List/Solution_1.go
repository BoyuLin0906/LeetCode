/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 1 ms / Beats 75.70%
Memory 2.94 MB / Beats 58.80%
*/
func deleteNode(node *ListNode) {
    
    node.Val = node.Next.Val
    node.Next = node.Next.Next
}