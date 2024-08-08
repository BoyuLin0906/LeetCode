/*
Runtime 4 ms / Beats 86.67%
Memory 6.60 MB / Beats 66.67%
*/

func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
    total_step := 1
    step := 0
    corner_count := 0
    direction := "right"
    next_direction := map[string]string{"right": "down",
                                        "down" : "left",
                                        "left" : "up",
                                        "up"   : "right"}

    res := make([][]int, 0, rows * cols)
    res = append(res, []int{rStart, cStart})

    cur_row := rStart
    cur_col := cStart
    for len(res) < rows * cols {
        if direction == "right" {
            cur_col++
        } else if direction == "left" {
            cur_col--
        } else if direction == "up" {
            cur_row--
        } else {
            cur_row++
        }

        if cur_row > -1 && cur_row < rows && cur_col > -1 && cur_col < cols {
            res = append(res, []int{cur_row, cur_col})
        }

        step++
        if total_step == step {
            direction = next_direction[direction]
            step = 0
            corner_count++
            if corner_count == 2 {
                total_step++
                corner_count = 0
            }
        }
    }

    return res
}