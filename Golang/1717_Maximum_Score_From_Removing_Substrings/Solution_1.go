/*
Runtime 23 ms / Beats 88.89%
Memory 7.34 MB / Beats 77.78%
*/

func maximumGain(s string, x int, y int) int {
    first_pass_stack := make([]rune, 0, len(s))
    first_pass_substring := []rune{'a', 'b'}
    second_pass_substring := []rune{'b', 'a'}
    first_pass_point := x
    second_pass_point := y
    res := 0

    if x < y {
        first_pass_substring, second_pass_substring = second_pass_substring, first_pass_substring
        first_pass_point, second_pass_point = second_pass_point, first_pass_point
    }

    for _, char := range s {
        if len(first_pass_stack) > 0 && first_pass_stack[len(first_pass_stack)-1] == first_pass_substring[0] && char == first_pass_substring[1] {
            first_pass_stack = first_pass_stack[:len(first_pass_stack)-1]
            res += first_pass_point
            continue
        }
        first_pass_stack = append(first_pass_stack, char)
    }

    second_pass_stack := make([]rune, 0, len(first_pass_stack))
    for _, char := range first_pass_stack {
        if len(second_pass_stack) > 0 && second_pass_stack[len(second_pass_stack)-1] == second_pass_substring[0] && char == second_pass_substring[1] {
            second_pass_stack = second_pass_stack[:len(second_pass_stack)-1]
            res += second_pass_point
            continue
        }
        second_pass_stack = append(second_pass_stack, char)
    }

    return res
}