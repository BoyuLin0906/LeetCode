/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
    nodes := make([]*TreeNode, 0)
    nodes = append(nodes, root)
    sum := 0

    for len(nodes) > 0 {
        node := nodes[0]
        left_node := node.Left
        right_node := node.Right

        if left_node != nil {
            if left_node.Left == nil && left_node.Right == nil {
                sum += left_node.Val
            } else {
                nodes = append(nodes, left_node)
            }
        }

        if right_node != nil && !(right_node.Left == nil && right_node.Right == nil) {
            nodes = append(nodes, right_node)
        }
        nodes = nodes[1:len(nodes)]
    }
    return sum

}