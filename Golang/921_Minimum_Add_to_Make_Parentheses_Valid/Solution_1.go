/*
Runtime 1 ms / Beats 74.58%
Memory 2.24 MB / Beats 19.49%
*/

func minAddToMakeValid(s string) int {
    
    stack := make([]byte, 0, len(s))
    for _, char := range s {
        if len(stack) > 0 && stack[len(stack)-1] == '(' && char == ')' {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, byte(char))
        }
    }

    return len(stack)
}