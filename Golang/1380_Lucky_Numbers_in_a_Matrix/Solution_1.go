/*
Runtime 8 ms / Beats 97.22%
Memory 5.56 MB / Beats 27.78%
*/

func luckyNumbers (matrix [][]int) []int {
    row_len, col_len := len(matrix), len(matrix[0])
    horizontal_min := make([]int, row_len)
    vertical_max := make([]int, col_len)

    for i := 0; i < row_len; i++ {
        horizontal_min[i] = math.MaxInt
    }
    for i := 0; i < col_len; i++ {
        vertical_max[i] = math.MinInt
    }

    for i := 0; i < row_len; i++ {
        for j := 0; j < col_len; j++ {
            if matrix[i][j] < horizontal_min[i] {
                horizontal_min[i] = matrix[i][j]
            }
            if matrix[i][j] > vertical_max[j] {
                vertical_max[j] = matrix[i][j]
            }
        }
    }  

    res := make([]int, 0 , max(len(horizontal_min), len(vertical_max)))
    for _, h_val := range horizontal_min {
        for _, v_val := range vertical_max {
            if h_val == v_val {
                res = append(res, h_val)
                break
            }
        }
    }

    return res
}