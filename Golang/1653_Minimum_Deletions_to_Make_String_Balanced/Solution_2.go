/*
Runtime 23 ms / Beats 94.44%
Memory 8.38 MB / Beats 16.67%
*/

func minimumDeletions(s string) int {
    s_len := len(s)
    count_a_arr := make([]int, s_len)
    count_b_arr := make([]int, s_len)

    count_a := 0
    count_b := 0

    for i := 0; i < s_len; i++ {
        count_b_arr[i] = count_b
        if s[i] == 'b' {
            count_b++
        }

        count_a_arr[s_len-1-i] = count_a
        if s[s_len-1-i] == 'a' {
            count_a++
        }
    }

    res := s_len
    for i := 0; i < s_len; i++ {
        res = min(res, count_a_arr[i]+count_b_arr[i])
    }


    return res
}