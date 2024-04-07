/*
Runtime 1 ms / Beats 75.18%
Memory 2.17 MB / Beats 90.06%
*/

func maxDepth(s string) int {

    count := 0
    res := 0
    for _, char := range(s) {
        if char == '(' {
            count++
            res = max(res, count)
        } else if char == ')' {
            count--
        }
    }
    return res
}