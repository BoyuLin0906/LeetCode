func minRemoveToMakeValid(s string) string {
    bracket_stack := make([]int, 0)

    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            bracket_stack = append(bracket_stack, i)
        } else if s[i] == ')' {
            if len(bracket_stack) > 0 {
                bracket_stack = bracket_stack[:len(bracket_stack)-1]
            } else {
                s = s[:i] + s[i+1:]
                i--
            } 
        }
    }

    for len(bracket_stack) != 0 {
        index := bracket_stack[len(bracket_stack)-1]
        bracket_stack = bracket_stack[:len(bracket_stack)-1]
        s = s[:index] + s[index+1:]
    }
    
    return s
}