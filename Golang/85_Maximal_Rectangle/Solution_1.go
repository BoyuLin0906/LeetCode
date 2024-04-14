/*
Runtime 0 ms / Beats 100.00%
Memory 6.66 MB / Beats 18.82%
*/


func maximalRectangle(matrix [][]byte) int {
    matrix_h := len(matrix)
    matrix_w := len(matrix[0])
    matrix_heights := make([][]int, matrix_h)
    res := 0

    for i := 0; i < matrix_h; i++ {
        matrix_heights[i] = make([]int, matrix_w)
        for j := 0; j < matrix_w; j++ {
            if matrix[i][j] == '1' {
                if i > 0 {
                    matrix_heights[i][j] = matrix_heights[i-1][j] + 1
                } else {
                    matrix_heights[i][j] = 1
                }
            }
        }
        res = max(res, largestRectangleArea(matrix_heights[i]))
    } 
    return res
}


// from 84
func largestRectangleArea(heights []int) int {
    heights = append([]int{0}, heights...)
    heights = append(heights, 0)
    res := 0

    stack := make([]int, 0)
    for i := 0; i < len(heights); i++ {
        for len(stack) > 0 && heights[stack[len(stack)-1]] > heights[i] {
            pop_index := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            prev_index := stack[len(stack)-1]
            res = max(res, (i - prev_index - 1) * heights[pop_index])
        }
        stack = append(stack, i)
    }

    return res
}