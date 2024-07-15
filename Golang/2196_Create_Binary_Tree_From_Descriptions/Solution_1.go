/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 304 ms / Beats 91.18%
Memory 7.72 MB / Beats 97.06%
*/

type NodeInfo struct {
    Node *TreeNode
    IsParent bool
    IsChild bool
}

func createBinaryTree(descriptions [][]int) *TreeNode {
    node_table := make(map[int]*NodeInfo, 0)
    
    for _, description := range descriptions {
        parent := description[0]
        child := description[1]
        
        is_left := false
        if description[2] == 1 {
            is_left = true
        }

        if _, ok := node_table[child]; !ok {
            node := &TreeNode{Val: child}
            node_table[child] = &NodeInfo{Node: node}
        }
        node_table[child].IsChild = true

        if _, ok := node_table[parent]; !ok {
            node := &TreeNode{Val: parent}
            node_table[parent] = &NodeInfo{Node: node}
        }
        node_table[parent].IsParent = true

        if is_left {
            node_table[parent].Node.Left = node_table[child].Node
        } else {
            node_table[parent].Node.Right = node_table[child].Node
        }
    }

    var res_node *TreeNode
    for _, info := range node_table {
        if info.IsParent == true && info.IsChild == false {
            res_node = info.Node
            break
        }
    }

    return res_node
}