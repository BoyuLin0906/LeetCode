/*
Runtime 0 ms / Beats 100.00%
Memory 6.32 MB / Beats 80.00%
*/

func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {

    step := 1 
    direction := 0
    direction_mapping := [][]int{[]int{0, 1},
                                 []int{1, 0},
                                 []int{0, -1},
                                 []int{-1, 0}}

    res := make([][]int, 0, rows * cols)

    cur_row := rStart
    cur_col := cStart
    for len(res) < rows * cols {
        for i := 0; i < 2; i++ {
            for j := 0; j < step; j++ {
                if cur_row > -1 && cur_row < rows && cur_col > -1 && cur_col < cols {
                    res = append(res, []int{cur_row, cur_col})
                }
                cur_row += direction_mapping[direction][0]
                cur_col += direction_mapping[direction][1]
            } 
            direction = (direction + 1) % 4 
        }
        step++
    }

    return res
}