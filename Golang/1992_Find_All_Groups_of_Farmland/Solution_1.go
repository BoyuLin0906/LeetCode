/*
Runtime 107 ms / Beats 100.00%
Memory 11.24 MB /Beats 90.00%
*/

func findFarmland(land [][]int) [][]int {
    
    res_list := make([][]int,0)

    for i := 0; i < len(land); i++ {
        for j := 0; j < len(land[0]); j++ {
            if land[i][j] == 1 {
                xMax, yMax := -1, -1
                helper(land, j, i, &xMax, &yMax)
                res_list = append(res_list, []int{i, j, yMax, xMax})
            }
        }
    }

    return res_list
}

func helper(land [][]int, x int, y int, xMax *int, yMax *int)  {

    if y == len(land) || x == len(land[0]) || land[y][x] == 0 {
            return
    }

    land[y][x] = 0
    if x > *xMax {
        *xMax = x
    }
    if y > *yMax {
        *yMax = y
    }

    helper(land, x+1, y, xMax, yMax)
    helper(land, x, y+1, xMax, yMax)
}