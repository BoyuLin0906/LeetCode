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
 Memory 2.34 MB / Beats 93.94%
 */
func bstToGst(root *TreeNode) *TreeNode {
    sum := 0
    helper(root, &sum)
    return root
}

func helper(node *TreeNode, sum *int) {
    if node == nil {
        return 
    }

    helper(node.Right, sum)
    *sum += node.Val
    node.Val = *sum
    helper(node.Left, sum)
}