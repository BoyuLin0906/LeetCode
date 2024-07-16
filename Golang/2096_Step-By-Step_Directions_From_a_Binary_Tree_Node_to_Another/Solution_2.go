/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func getDirections(root *TreeNode, startValue int, destValue int) string {
    start_path := make([]rune, 0)
    end_path := make([]rune, 0)

    find_path(root, startValue, &start_path)
    find_path(root, destValue, &end_path)

    count := 0
    for count < len(start_path) && count < len(end_path) && start_path[count] == end_path[count] {
        count += 1
    }

    res_path := make([]rune, 0, len(start_path)+len(end_path))
    for i := 0; i < len(start_path)-count; i++ {
        res_path = append(res_path, 'U')
    }
     for i := count; i < len(end_path); i++ {
        res_path = append(res_path, end_path[i])
    }

    return string(res_path)
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
