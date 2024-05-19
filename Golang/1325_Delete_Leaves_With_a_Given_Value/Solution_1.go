/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 2 ms / Beats 81.63%
Memory 5.05 MB / Beats 91.11%
*/

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    if root == nil {
        return nil
    }

    root.Left = removeLeafNodes(root.Left, target)
    root.Right = removeLeafNodes(root.Right, target)

    if root.Left == nil && root.Right == nil && root.Val == target {
        return nil
    }
    
    return root
}