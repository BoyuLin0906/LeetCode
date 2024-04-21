/*
Runtime 0 ms / Beats 100.00%
Memory 3.97 MB / Beats 73.48%
*/

func numIslands(grid [][]byte) int {
    res := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == '1' {
                res += 1
                helper(grid, j, i)
            }
        }
    }
    return res
}

func helper(grid [][]byte, x int, y int) {
    if x < 0 || x >= len(grid[0]) || y < 0 || y >= len(grid) || grid[y][x] == '0' {
        return
    }

    grid[y][x] = '0'
    helper(grid, x-1, y)
    helper(grid, x+1, y)
    helper(grid, x, y-1)
    helper(grid, x, y+1)
}