func removeKdigits(num string, k int) string {
    if len(num) == k {
        return "0"
    }

    stack := make([]rune, 0)
    for _, n := range num {
        for k > 0 && len(stack) > 0 && stack[len(stack)-1] > n {
            stack = stack[:len(stack)-1]
            k--
        }
        stack = append(stack, n)
    }

    for k > 0 {
        stack = stack[:len(stack)-1]
        k--
    }

    for len(stack) > 0 && stack[0] == '0' {
        stack = stack[1:len(stack)]
    }

    if len(stack) == 0 {
        return "0"
    }

    return string(stack)
}