/*
Runtime 272 ms / Beats 5.88%
Memory 3.84 MB / Beats 74.12%
*/

func maximalRectangle(matrix [][]byte) int {
    matrix_h := len(matrix)
    matrix_w := len(matrix[0])
    res := 0

    for i := 0; i < matrix_h; i++ {
        for j := 0; j < matrix_w; j++ {
            res = max(res, largestArea(matrix, matrix_w, matrix_h, j, i))
        }
    } 
    return res
}

func largestArea(matrix [][]byte, width int, height int, x int, y int ) int {
    y_len := 0
    res := 0
    min_right_len := 201
    for y < height {
        if matrix[y][x] == '0'{
            break
        }
        min_right_len = min(min_right_len, countRightLen(matrix, width, x, y))
        y++
        y_len++
        res = max(res, (y_len * min_right_len))
    }

    return res
}

func countRightLen(matrix [][]byte, width int, x int, y int) int {
    res := 0
    for x < width {
        if matrix[y][x] == '0' {
            break
        } else {
            res++
            x++
        }
    }
    return res
}