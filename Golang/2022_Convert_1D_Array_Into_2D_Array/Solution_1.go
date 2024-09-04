/*
Runtime 92 ms / Beats 87.30%
Memory 7.81 MB / Beats 76.44%
*/

func construct2DArray(original []int, m int, n int) [][]int {

    if len(original) != m * n {
        return [][]int{}
    }

    array_2d := make([][]int, m)
    for i := 0; i < m; i++ {
        array_2d[i] = make([]int, n)
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            array_2d[i][j] = original[i*n+j]
        }
    }

    return array_2d
}