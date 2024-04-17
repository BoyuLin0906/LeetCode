/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 0 ms / Beats 100.00%
Memory 5.78 MB / Beats 100.00%
*/
 
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    head := TreeNode{Val: val, Left: root}
    if depth == 1 {
        return &head
    }
    helper(root, val, depth-1)
    return head.Left
}

func helper(node *TreeNode, val int, depth int) {
    if depth == 1 {
        node.Left = &TreeNode{Val: val, Left: node.Left}
        node.Right = &TreeNode{Val: val, Right: node.Right}
        return
    }

    if node.Left != nil {
        helper(node.Left, val, depth-1)
    }
    if node.Right != nil {
        helper(node.Right, val, depth-1)
    }
}