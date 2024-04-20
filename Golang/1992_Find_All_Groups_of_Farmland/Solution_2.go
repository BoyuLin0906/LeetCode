/*
Runtime 119 ms / Beats 80.00%
Memory 11.03 MB /Beats 90.00%
*/

func findFarmland(land [][]int) [][]int {
    
    res_list := make([][]int,0)

    for i := 0; i < len(land); i++ {
        for j := 0; j < len(land[0]); j++ {
            if land[i][j] == 1 {
                res := helper(land, j, i)
                res_list = append(res_list, res)
            }
        }
    }

    return res_list
}

func helper(land [][]int, x int, y int) []int {
    res := []int{y, x}
    temp_x, temp_y := x, y
    
    for temp_y < len(land) && land[temp_y][x] == 1 {
        temp_y++
    }
    for temp_x < len(land[0]) && land[y][temp_x] == 1 {
        temp_x++
    }

    for i := y; i < temp_y; i++ {
        for j := x; j < temp_x; j++ {
            land[i][j] = 0
        }
    }

    res = append(res, temp_y-1, temp_x-1)
    return res
}