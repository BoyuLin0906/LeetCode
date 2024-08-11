/*
Runtime 0 ms / Beats 100.00%
Memory 5.37 MB / Beats 11.11%
*/

// Pixelation (e.g. Number of Islands)
func regionsBySlashes(grid []string) int {
    region_map := make([][]int, len(grid) * 3)
    for i := 0; i < len(grid) * 3; i++ {
        region_map[i] = make([]int, len(grid) * 3)
    }

    for i := 0; i < len(grid); i++ {
        j := 0
        for j < len(grid) {
            if grid[i][j] == '/' {
                region_map[i * 3][j * 3 + 2] = 1
                region_map[i * 3 + 1][j * 3 + 1] = 1
                region_map[i * 3 + 2][j * 3] = 1
            } else if grid[i][j] == '\\' {
                region_map[i * 3][j * 3] = 1
                region_map[i * 3 + 1][j * 3 + 1] = 1
                region_map[i * 3 + 2][j * 3 + 2] = 1
            }
            j += 1
        }
    }

    res_nums := 0
    for i := 0; i < len(region_map); i++ {
        for j := 0; j < len(region_map); j++ {
            if region_map[i][j] == 0 {
                res_nums++
                dfs(region_map, i, j)
            }
        }
    }

    return res_nums
}

func dfs(region_map [][]int, y int, x int) {
    if x < 0 || x >= len(region_map) || y < 0 || y >= len(region_map) || region_map[y][x] == 1 {
        return
    }
    region_map[y][x] = 1
    dfs(region_map, y+1, x)
    dfs(region_map, y-1, x)
    dfs(region_map, y, x+1)
    dfs(region_map, y, x-1)
}