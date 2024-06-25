/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

  /*
 Runtime 1 ms / Beats 66.67%
 Memory 2.37 MB / Beats 93.94%
 */
func bstToGst(root *TreeNode) *TreeNode {
    sum := 0
    stack := make([]*TreeNode, 0)
    node := root

    for node != nil || len(stack) > 0 {
        for node != nil {
            stack = append(stack, node)
            node = node.Right
        }

        node = stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        sum += node.Val
        node.Val = sum
        node = node.Left
    }

    return root
}