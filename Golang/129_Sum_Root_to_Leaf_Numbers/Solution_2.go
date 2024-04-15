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
Memory 2.41 MB /Beats 6.15%
*/

func sumNumbers(root *TreeNode) int {
    return dfsHelper(root, 0)
}

func dfsHelper(node *TreeNode, num int) int {
    num = num * 10 + node.Val
    if node.Left == nil && node.Right == nil {
        return num
    }

    sum := 0
    if node.Left != nil {
        sum += dfsHelper(node.Left, num) 
    }
    if node.Right != nil {
        sum += dfsHelper(node.Right, num) 
    }
    return sum
}