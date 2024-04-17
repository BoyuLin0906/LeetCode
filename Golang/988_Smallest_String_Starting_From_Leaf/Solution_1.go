/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 
var smallest_str = ""

func smallestFromLeaf(root *TreeNode) string {
    smallest_str = ""
    helper(root, "")
    return smallest_str
}

func helper(node *TreeNode, node_str string) {
    node_str = string(node.Val + 'a') + node_str
    
    if node.Left == nil && node.Right == nil {
        if smallest_str == "" || smallest_str > node_str {
            smallest_str = node_str
            return
        }
    }

    if node.Left != nil {
        helper(node.Left, node_str)
    } 
    if node.Right != nil {
        helper(node.Right, node_str)
    }
}