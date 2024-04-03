/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 * 
 *  Runtime 115 ms / Beats 83.36%
 *  Memory 8.50 MB / Beats 75.70%
 * 
 */
func isPalindrome(head *ListNode) bool {
    nodeList := findMidNode(head)
    nodeList = reverse(nodeList)
    return compare(head, nodeList)
}

func findMidNode(node *ListNode) *ListNode {
    // O(n/2) = O(n)
    slow_node, fast_node := node, node
    for fast_node != nil && fast_node.Next != nil {
        slow_node = slow_node.Next
        fast_node = fast_node.Next.Next
    }
    return slow_node
}

func reverse(node *ListNode)  *ListNode {
    // O(n/2) = O(n)
    var prevNode *ListNode
    currNode := node
    for currNode != nil {
        tempNode := currNode.Next
        currNode.Next = prevNode
        prevNode = currNode
        currNode = tempNode
    }
    return prevNode
}

func compare(node_1 *ListNode, node_2 *ListNode) bool {
    // O(n/2) = O(n)
    for node_1 != nil && node_2 != nil {
        if node_1.Val != node_2.Val {
            return false
        }
        node_1 = node_1.Next
        node_2 = node_2.Next
    }
    return true
}