/*
Runtime 2 ms / Beats 82.76%
Memory 2.14 MB / Beats 72.41%
*/

func judgeSquareSum(c int) bool {

    left_idx := 0
    right_idx := int(math.Sqrt(float64(c)))

    for left_idx <= right_idx {
        tmp_c := left_idx * left_idx + right_idx * right_idx
        if tmp_c == c {
            return true
        }

        if tmp_c < c {
            left_idx += 1
        } else {
            right_idx -= 1
        }
    }
    return false
}