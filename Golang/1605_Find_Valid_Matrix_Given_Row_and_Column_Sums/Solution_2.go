/*
Runtime 61 ms / Beats 87.34%
Memory 16.58 MB / Beats 19.63%
*/

func restoreMatrix(rowSum []int, colSum []int) [][]int {

    row_len := len(rowSum)
    col_len := len(colSum)
    res := make([][]int, 0, row_len)

    for i := 0; i < row_len; i++ {
        col := make([]int, col_len)
        res = append(res, col)
    }

    i := 0
    j := 0

    for i < row_len && j < col_len {
        res[i][j] = min(rowSum[i], colSum[j])
        rowSum[i] -= res[i][j]
        colSum[j] -= res[i][j]
        if rowSum[i] == 0 {
            i += 1
        } else {
            j += 1
        }
    }

    return res
}