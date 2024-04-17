/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type nodeObject struct {
    Node *TreeNode
    Str string
}

func smallestFromLeaf(root *TreeNode) string {
    queue := make([]*nodeObject, 0)
    queue = append(queue, &nodeObject{Node: root, Str: ""})
    smallest_str := ""

    for len(queue) > 0 {
        object := queue[0]
        queue = queue[1:len(queue)]
        node_str := string(object.Node.Val + 'a') + object.Str
        
        if object.Node.Left == nil && object.Node.Right == nil {
            if smallest_str == "" || smallest_str > node_str {
                smallest_str = node_str
                continue
            }
        }

        if object.Node.Left != nil {
            queue = append(queue, &nodeObject{Node: object.Node.Left, Str: node_str})
        } 
        if object.Node.Right != nil {
            queue = append(queue, &nodeObject{Node: object.Node.Right, Str: node_str})
        }
    }

    return smallest_str
}