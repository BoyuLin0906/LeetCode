/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
 Runtime 3 ms / Beats 77.78%
 Memory 3.25 MB / Beats 92.59%
*/
func distributeCoins(root *TreeNode) int {
    _, move := helper(root) 
    return move
}

func helper(node *TreeNode) (int, int) {
    if node == nil {
        return 0, 0
    }

    left_coin, left_move := helper(node.Left)
    right_coin, right_move := helper(node.Right)

    move := abs(left_coin) + abs(right_coin) + left_move + right_move
    return (node.Val - 1) + left_coin + right_coin, move
}

func abs(n int) int {
	return int(math.Abs(float64(n)))
}