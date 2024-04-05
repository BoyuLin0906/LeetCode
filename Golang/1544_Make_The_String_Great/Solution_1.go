type Stack []byte

func (s *Stack) CheckEmpty() bool {
    return len(*s) == 0
}

func (s *Stack) Push(letter byte) {
    *s = append(*s, letter)
}

func (s *Stack) Pop() (byte, bool) {
    if s.CheckEmpty() {
        return 0, false
    } else {
        index := len(*s) - 1
        value := (*s)[index]
        *s = (*s)[:index]
        return value, true
    }
}

func (s *Stack) ShowTop() (byte, bool) {
    if s.CheckEmpty() {
        return 0, false
    } else {
        return (*s)[len(*s) - 1], true
    }
}

func makeGood(s string) string {
    var stack Stack

    for i := 0; i < len(s) ; i++ {
        top_val, notEmpty := stack.ShowTop()
        if !notEmpty {
            stack.Push(s[i])
            continue
        } 
        if top_val - s[i] == 32 || s[i] - top_val == 32 {
            stack.Pop()
            continue
        } 

        stack.Push(s[i])
    }
    
    res := ""
    for !stack.CheckEmpty() {
        val, _ := stack.Pop()
        res = string(val) + res
    }

    return res
}