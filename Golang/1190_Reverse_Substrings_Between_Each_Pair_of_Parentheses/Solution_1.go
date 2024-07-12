/*
Runtime 0 ms / Beats 100.00%
Memory 2.53 MB / Beats 20.00%
*/

func reverseParentheses(s string) string {
    stack := make([]byte, 0, len(s))

    for i := 0; i < len(s); i++ {
        if s[i] == ')' {
            inter_stack := make([]byte, 0, len(stack))
            for stack[len(stack)-1] != '(' {
                pop_val := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                inter_stack = append(inter_stack, pop_val)
            }
            stack = stack[:len(stack)-1]
            for _, val := range inter_stack {
                stack = append(stack, val)
            }
        } else {
            stack = append(stack, s[i])
        }
    }

    return string(stack)
}