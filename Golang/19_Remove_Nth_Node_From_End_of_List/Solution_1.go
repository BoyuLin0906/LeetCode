/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    res := &ListNode{Val: -1, Next: head}
    pointer_1, pointer_2 := head, res
    list_len := 0

    for pointer_1 != nil {
        list_len += 1
        pointer_1 = pointer_1.Next
    }

    count := list_len - n
    for count > 0 {
        count--
        pointer_2 = pointer_2.Next
    }

    if pointer_2.Next != nil {
        pointer_2.Next = pointer_2.Next.Next
    }
    return res.Next
}