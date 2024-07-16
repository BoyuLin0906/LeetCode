/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Runtime 233 ms / Beats 68.42%
Memory 35.92 MB / Beats 94.74%
*/

func getDirections(root *TreeNode, startValue int, destValue int) string {

    lca_node := findLowestCommonAncestor(root, startValue, destValue)
    
    start_path := make([]rune, 0)
    end_path := make([]rune, 0)

    find_path(lca_node, startValue, &start_path)
    find_path(lca_node, destValue, &end_path)
    
    res_path := make([]rune, 0, len(start_path)+len(end_path))
    for i := 0; i < len(start_path); i++ {
        res_path = append(res_path, 'U')
    }
    for _, dir := range end_path {
        res_path = append(res_path, dir)
    }

    return string(res_path)
}

func findLowestCommonAncestor(root *TreeNode, startValue int, destValue int) *TreeNode {

    if  root == nil || root.Val == startValue || root.Val == destValue {
        return root
    }

    left_lca_node := findLowestCommonAncestor(root.Left, startValue, destValue)
    right_lca_node := findLowestCommonAncestor(root.Right, startValue, destValue)

    if left_lca_node == nil {
        return right_lca_node
    } else if right_lca_node == nil {
        return left_lca_node
    }

    return root
}

func find_path(root *TreeNode, tagert_val int, path *[]rune) bool {

    if root == nil {
        return false
    }
    
    if tagert_val == root.Val {
        return true
    }

    *path = append(*path, 'L')
    if find_path(root.Left, tagert_val, path) {
        return true
    }
    *path = (*path)[:len(*path)-1]
    
    *path = append(*path, 'R')
    if find_path(root.Right, tagert_val, path) {
        return true
    }
    *path = (*path)[:len(*path)-1]

    return false
}
