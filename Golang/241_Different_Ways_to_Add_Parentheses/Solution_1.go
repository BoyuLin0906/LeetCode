/*
Runtime 1 ms / Beats 71.43%
Memory 2.36 MB / Beats 84.13%
*/

func diffWaysToCompute(expression string) []int {
    res := make([]int, 0)
    
    for idx, char := range expression {
        if char == '+' || char == '-' || char == '*' {
            left_res := diffWaysToCompute(expression[:idx])
            right_res := diffWaysToCompute(expression[idx+1:])

            for _, left_val := range left_res {
                for _, right_val := range right_res {
                    if char == '+' {
                        res = append(res, left_val + right_val)
                    } else if char == '-' {
                        res = append(res, left_val - right_val)
                    } else {
                        res = append(res, left_val * right_val)
                    }
                }
            }
        }
    }

    if len(res) == 0 {
        val, _ := strconv.Atoi(expression)
        res = append(res, val)
    }
    return res
}