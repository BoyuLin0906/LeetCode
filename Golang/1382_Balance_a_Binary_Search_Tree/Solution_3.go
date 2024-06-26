/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 44 ms / Beats 61.33%
Memory 7.35 MB / Beats 82.67%
*/
func balanceBST(root *TreeNode) *TreeNode {
    
    node_vals := make([]int, 0)
    order_helper(root, &node_vals)

    res_node := create_helper(node_vals, 0, len(node_vals)-1)
    return res_node
}

func order_helper(node *TreeNode, node_vals *[]int) {
    if node == nil {
        return
    }

    order_helper(node.Left, node_vals)
    *node_vals = append(*node_vals, node.Val)
    order_helper(node.Right, node_vals)
}

func create_helper(node_vals []int, start int, end int) *TreeNode {

    if start > end {
        return nil
    }

    mid := start + (end - start) / 2
    left_sub_tree := create_helper(node_vals, start, mid-1)
    right_sub_tree := create_helper(node_vals, mid+1, end)

    return &TreeNode{Val: node_vals[mid], Left: left_sub_tree, Right: right_sub_tree}
}