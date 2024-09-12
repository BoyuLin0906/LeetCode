/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

/*
Runtime 2 ms / Beats 71.11%
Memory 3.80 MB / Beats 48.89%
*/
func copyRandomList(head *Node) *Node {
    node_table := make(map[*Node]*Node, 0)

    curr_head := head
    for curr_head != nil {
        new_node := &Node{Val: curr_head.Val}
        node_table[curr_head] = new_node
        curr_head = curr_head.Next
    }

    curr_head = head
    dummy_head := &Node{Val: -1}
    temp_head := dummy_head 
    for curr_head != nil { 
        curr_node := node_table[curr_head]
        curr_node.Next = node_table[curr_head.Next]
        curr_node.Random = node_table[curr_head.Random] 
        temp_head.Next = curr_node
        temp_head = temp_head.Next
        curr_head = curr_head.Next
    }
    return dummy_head.Next
}