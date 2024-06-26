/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 40 ms / Beats 76.00%
Memory 7.50 MB / Beats 70.67%
*/
func balanceBST(root *TreeNode) *TreeNode {
    
    node_vals := make([]int, 0)
    queue := make([]*TreeNode, 0)
    queue = append(queue, root)

    for len(queue) > 0 {
        node := queue[0]
        node_vals = append(node_vals, node.Val)
        queue = queue[1:]
        
        if node.Left != nil {
            queue = append(queue, node.Left)
        }
        if node.Right != nil {
            queue = append(queue, node.Right)
        }
    }
    sort.Ints(node_vals)
    dummy_node := &TreeNode{Val:-1, Left: &TreeNode{}}
    helper(node_vals, dummy_node.Left, 0, len(node_vals)-1)

    return dummy_node.Left
}

func helper(node_vals []int, node *TreeNode, start int, end int) bool {

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
    if !helper(node_vals, node.Left, start, mid-1) {
         node.Left = nil
    }
    if !helper(node_vals, node.Right, mid+1, end) {
        node.Right = nil
    }
    
    return true
}