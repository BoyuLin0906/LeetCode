/*
Runtime 21 ms / Beats 6.10%
Memory 7.73 MB / Beats 7.32%
*/

func checkValidString(s string) bool {
    s_len := len(s)
    check_table := make(map[int]map[int]int)
    for i := 0; i < s_len; i++ {
        check_table[i] = make(map[int]int)
        for j := 0; j < s_len; j++ {
            check_table[i][j] = -1
        }
    }
    return helper(s,s_len, 0, 0, check_table)
}

func helper(s string, s_len int, index int, count int, check_table map[int]map[int]int) bool{
    if s_len == index {
        return count == 0
    }

    if check_table[index][count] != -1 {
        return check_table[index][count] == 1
    }

    is_valid := false
    if s[index] == '*' {
        if count > 0 {
            is_valid = is_valid || helper(s, s_len, index+1, count-1, check_table)
        }
        is_valid = is_valid || helper(s, s_len, index+1, count+1, check_table)
        is_valid = is_valid || helper(s, s_len, index+1, count, check_table)
    } else {
        if s[index] == '(' {
            is_valid = helper(s, s_len, index+1, count+1, check_table)
        } else if s[index] == ')' && count > 0 {
            is_valid = helper(s, s_len, index+1, count-1, check_table)
        }
    }

    if is_valid {
        check_table[index][count] = 1
    } else {
        check_table[index][count] = 0
    }
    return is_valid
}
