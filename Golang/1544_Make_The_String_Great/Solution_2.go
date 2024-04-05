func makeGood(s string) string {
    if len(s) <= 1 {
        return s
    }

    stack := make([]byte, 0)
    for i := 0; i < len(s) ; i++ {
		s_len := len(stack) 
		if s_len > 0 && ((s[i]-stack[s_len-1] == 32) || (stack[s_len-1]-s[i] == 32)) {
			stack = stack[:s_len-1]
		} else {
			stack = append(stack, s[i])
		}
	}
	return string(stack)
}