/*
 Runtime 2 ms / Beats 88.89%
 Memory 2.34 MB / Beats 88.89%
*/
func matrixScore(grid [][]int) int {
    row_len := len(grid)
    col_len := len(grid[0])
    // first bit needs to be 1
    res := row_len * (1 << (col_len-1))
    // other bits need to get max `1`
    for i := 1; i < col_len; i++ {
        count := 0
        for j := 0; j < row_len; j++ {
            if grid[j][0] == grid[j][i] {
                count++
            }
        }
        res += max(count, row_len-count) * (1 << (col_len-1-i))
    }

    return res
}