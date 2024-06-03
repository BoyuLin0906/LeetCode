/*
Runtime 0 ms / Beats 100.00%
Memory 6.00 MB / Beats 59.09%
*/

func appendCharacters(s string, t string) int {
    s_ptr := 0
    t_prt := 0

    for s_ptr < len(s) && t_prt < len(t) {
        if s[s_ptr] == t[t_prt] {
            t_prt++
        } 
        s_ptr++
    }
    return len(t) - t_prt
}