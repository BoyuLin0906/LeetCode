/*
Runtime 0 ms / Beats 100.00%
Memory 4.46 MB / Beats 62.50%
*/

func islandPerimeter(grid [][]int) int {
    col_len := len(grid)
    row_len := len(grid[0])
    res := 0

    for i := 0; i < col_len; i++ {
        for j := 0; j < row_len; j++ {
            if grid[i][j] == 0 {
                continue
            }
            
            count := 4
            if i > 0 && grid[i-1][j] == 1 {
                count--
            }
            if i < col_len-1 && grid[i+1][j] == 1 {
                count--
            }
            if j > 0 && grid[i][j-1] == 1 {
                count--
            }
            if j < row_len-1 && grid[i][j+1] == 1 {
                count--
            }
            res += count
        }
    }
    return res
}