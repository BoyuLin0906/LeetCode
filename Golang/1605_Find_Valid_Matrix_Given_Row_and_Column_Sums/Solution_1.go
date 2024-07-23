/*
Runtime 73 ms / Beats 44.06%
Memory 20.71 MB / Beats 7.36%
*/

func restoreMatrix(rowSum []int, colSum []int) [][]int {

    row_len := len(rowSum)
    col_len := len(colSum)
    res := make([][]int, 0, row_len)

    for i := 0; i < row_len; i++ {
        col := make([]int, col_len)
        res = append(res, col)
    }

    for i := 0; i < row_len; i++ {
        for j := 0; j < col_len; j++ {
            val := min(rowSum[i], colSum[j])
            res[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val
        }
    }

    return res
}