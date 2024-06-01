/*
Runtime 0 ms / Beats 100.00%
Memory 2.28 MB / Beats 91.16%
*/

func scoreOfString(s string) int {

    res := 0
    for i := 1; i < len(s); i++ {
        tmp := int(s[i]) - int(s[i-1])
        if tmp < 0 {
            tmp = -tmp
        }
        res += tmp
    }
    return res

}