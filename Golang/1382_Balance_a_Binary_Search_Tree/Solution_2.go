/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 42 ms / Beats 66.67%
Memory 7.77 MB / Beats 44.00%
*/
func balanceBST(root *TreeNode) *TreeNode {
    
    node_vals := make([]int, 0)
    order_helper(root, &node_vals)
    
    dummy_node := &TreeNode{Val:-1, Left: &TreeNode{}}
    create_helper(node_vals, dummy_node.Left, 0, len(node_vals)-1)

    return dummy_node.Left
}

func order_helper(node *TreeNode, node_vals *[]int) {
    if node == nil {
        return
    }

    order_helper(node.Left, node_vals)
    *node_vals = append(*node_vals, node.Val)
    order_helper(node.Right, node_vals)
}

func create_helper(node_vals []int, node *TreeNode, start int, end int) bool {

    mid := (start + end) / 2
    if node_vals[mid] == -1 {
        return false
    }

    node.Val = node_vals[mid]
    node_vals[mid] = -1
    if start == end {
        return true
    }

    node.Left = &TreeNode{}
    node.Right = &TreeNode{}
    if !create_helper(node_vals, node.Left, start, mid-1) {
         node.Left = nil
    }
    if !create_helper(node_vals, node.Right, mid+1, end) {
        node.Right = nil
    }
    
    return true
}