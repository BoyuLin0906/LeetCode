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
Memory 2.40 MB /Beats 36.67%
*/

type nodeObject struct {
    Node *TreeNode
    Num int
}

func sumNumbers(root *TreeNode) int {
    queue := make([]nodeObject, 0)
    queue = append(queue, nodeObject{Node: root, Num: 0})
    res := 0

    for len(queue) > 0 {
        node_obj := queue[0]
        queue = queue[1:len(queue)]
        num := node_obj.Num * 10 + node_obj.Node.Val

        if node_obj.Node.Left == nil && node_obj.Node.Right == nil {
            res += num
        } else {
            if node_obj.Node.Left != nil {
                node := nodeObject{Node: node_obj.Node.Left, Num: num}
                queue = append(queue, node)
            } 
            if node_obj.Node.Right != nil {
                node := nodeObject{Node: node_obj.Node.Right, Num: num}
                queue = append(queue, node)
            }
        }
    }

    return res
}