func minRemoveToMakeValid(s string) string {
    bracket_stack := make([]int, 0)
    byte_res := []byte(s)

    for i := 0; i < len(byte_res); i++ {
        if s[i] == '(' {
            bracket_stack = append(bracket_stack, i)
        } else if s[i] == ')' {
            if len(bracket_stack) > 0 {
                bracket_stack = bracket_stack[:len(bracket_stack)-1]
            } else {
                byte_res[i] = '*'
            } 
        }
    }

    for len(bracket_stack) != 0 {
        index := bracket_stack[len(bracket_stack)-1]
        bracket_stack = bracket_stack[:len(bracket_stack)-1]
        byte_res[index] = '*'
    }
    
    return strings.Replace(string(byte_res), "*", "", -1)
}