/*
Runtime 8 ms / Beats 97.22%
Memory 5.47 MB / Beats 66.67%
*/

func luckyNumbers (matrix [][]int) []int {
    row_len, col_len := len(matrix), len(matrix[0])
    r_min_max := math.MinInt
    c_max_min := math.MaxInt

    for i := 0; i < row_len; i++ {
        r_min := slices.Min(matrix[i])
        r_min_max = max(r_min, r_min_max)
    }

    for i := 0; i < col_len; i++ {
        c_max := math.MinInt
        for j := 0; j < row_len; j++ {
            c_max = max(c_max, matrix[j][i])
        }
        c_max_min = min(c_max, c_max_min)
    }


    res := make([]int, 0 , 1)
    if r_min_max == c_max_min {
        res = append(res, r_min_max)
    }

    return res
}