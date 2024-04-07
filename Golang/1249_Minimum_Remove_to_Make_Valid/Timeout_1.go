func minRemoveToMakeValid(s string) string {
    stack := make([]rune, 0)
    bracket_count := 0 

    for _, char := range s {
        if char == '(' {
            bracket_count++
            stack = append(stack, char)
        } else if char == ')' && bracket_count > 0 {
            bracket_count--
            stack = append(stack, char)
        } else if char != ')' && char != '('{
            stack = append(stack, char)
        }
    }

    res := ""
    for len(stack) != 0 {
        val := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if val == '(' && bracket_count > 0 {
            bracket_count--
            continue
        }
        res = string(val) + res
    }
    
    return res
}