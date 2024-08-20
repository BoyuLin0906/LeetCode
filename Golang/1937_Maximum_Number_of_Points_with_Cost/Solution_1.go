/*
Runtime 150 ms / Beats 90.71%
Memory 16.91 MB / Beats 32.35%
*/

func maxPoints(points [][]int) int64 {

    row_len := len(points)
    col_len := len(points[0])
    prev_row := make([]int, col_len)
    res := 0

    for i := 0; i < row_len; i++ {
        cur_row := make([]int, col_len)

        left_max := 0
        for j := 0; j < col_len; j++ {
            left_max = max(left_max-1, prev_row[j])
            cur_row[j] = left_max
        }

        right_max := 0
        for j := col_len-1; j >= 0; j-- {
            right_max = max(right_max-1, prev_row[j])
            cur_row[j] = max(right_max, cur_row[j]) + points[i][j]
            prev_row[j] = cur_row[j]
            res = max(res, cur_row[j])
        }
    }

    return int64(res)
}