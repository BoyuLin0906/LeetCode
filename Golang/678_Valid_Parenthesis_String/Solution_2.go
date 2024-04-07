/*
Runtime 1 ms / Beats 86.59%
Memory 2.18 MB / Beats 60.98%
*/

func checkValidString(s string) bool {
    
    left_bracket_count, right_bracket_count := 0, 0
    s_len := len(s)

    for i := 0 ; i < s_len; i++ {
        if s[i] == '(' || s[i] == '*' {
            left_bracket_count++
        } else {
            left_bracket_count--
        }
        if left_bracket_count < 0 {
            return false
        }
    }

    for j := s_len - 1; j > -1; j-- {
        if s[j] == ')' || s[j] == '*' {
            right_bracket_count++
        } else {
            right_bracket_count--
        }
        if right_bracket_count < 0 {
            return false
        }
    } 

    return true
}

