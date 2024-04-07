func checkValidString(s string) bool {
    brackets_stack := make([]int, 0)
    asterisks_stack := make([]int, 0)

    for index, char := range s {
        if char == '*' {
            asterisks_stack = append(asterisks_stack, index)
            continue
        }

        if char == '(' {
            brackets_stack = append(brackets_stack, index)
            continue
        }

        if char == ')' {
            if len(brackets_stack) != 0 {
                brackets_stack = brackets_stack[:len(brackets_stack)-1]
            } else if len(asterisks_stack) != 0 {
                asterisks_stack = asterisks_stack[:len(asterisks_stack)-1]
            } else {
                return false
            }
        }

    }

    for len(brackets_stack) > 0 && len(asterisks_stack) > 0 {
        brackets_index := brackets_stack[len(brackets_stack)-1]
        asterisks_index := asterisks_stack[len(asterisks_stack)-1]
        if brackets_index > asterisks_index {
            return false
        }
        brackets_stack = brackets_stack[:len(brackets_stack)-1]
        asterisks_stack = asterisks_stack[:len(asterisks_stack)-1]
    }

    return len(brackets_stack) == 0
}

