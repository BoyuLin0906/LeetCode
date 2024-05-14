/*
Runtime 54 ms / Beats 88.89%
Memory 2.28 MB / Beats 88.89%
*/

func getMaximumGold(grid [][]int) int {
    row_len := len(grid)
    col_len := len(grid[0])
    res := 0
    for j := 0; j < row_len; j++ {
        for i := 0; i < col_len; i++ {
            res = max(res, helper(grid, i, j))
        }
    }
    return res
}


func helper(grid [][]int, x int, y int) int {
    row_len := len(grid)
    col_len := len(grid[0])

    if x >= col_len || x < 0 || y >= row_len || y < 0 || grid[y][x] == 0 {
        return 0
    }

    cur_grid_val := grid[y][x] 
    grid[y][x] = 0
    val := max(helper(grid, x, y-1),
               helper(grid, x, y+1),
               helper(grid, x-1, y),
               helper(grid, x+1, y))
    grid[y][x] = cur_grid_val
    
    return cur_grid_val + val
}