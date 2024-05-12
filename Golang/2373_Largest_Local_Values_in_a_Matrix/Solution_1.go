/*
Runtime 3 ms / Beats 96.43%
Memory 6.40 MB / Beats 42.86%
*/

func largestLocal(grid [][]int) [][]int {
    row_len := len(grid)
    col_len := len(grid[0])
    res := make([][]int, row_len-2)

    for y := 1; y < row_len-1; y++ {
        res[y-1] = make([]int, col_len-2)
        for x := 1; x < col_len-1; x++ {
            res[y-1][x-1] = max(grid[y-1][x], grid[y][x], grid[y+1][x],
                                grid[y-1][x-1], grid[y][x-1], grid[y+1][x-1],
                                grid[y-1][x+1], grid[y][x+1], grid[y+1][x+1])
        }
    }

    return res
    
}