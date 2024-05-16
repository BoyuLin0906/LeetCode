/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 5 ms / Beats 93.94%
Memory 6.15 MB / Beats 96.97%
*/
func evaluateTree(root *TreeNode) bool {
    if root.Left == nil && root.Right == nil {
        return root.Val == 1
    }

    if root.Val == 2 {
        return evaluateTree(root.Left) || evaluateTree(root.Right)
    } else {
        return evaluateTree(root.Left) && evaluateTree(root.Right)
    }
}