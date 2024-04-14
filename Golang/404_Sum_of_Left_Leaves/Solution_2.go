/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 2 ms / Beats 73.50%
Memory 2.84 MB / Beats 11.00%
*/
func sumOfLeftLeaves(root *TreeNode) int {
    return helper(root, false)
}

func helper(node *TreeNode, is_left bool) int {
    if node == nil {
        return 0
    }

    if is_left && node.Left == nil && node.Right == nil {
        return node.Val
    }

    return helper(node.Left, true) + helper(node.Right, false)
}