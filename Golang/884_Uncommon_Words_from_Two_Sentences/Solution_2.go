/*
Runtime 0 ms / Beats 100.00%
Memory 2.48 MB / Beats 77.16%
*/

func uncommonFromSentences(s1 string, s2 string) []string {
    s1_arr := strings.Split(s1, " ")
    s2_arr := strings.Split(s2, " ")

    counter := make(map[string]int, 0)
    for _, str := range s1_arr {
        counter[str] += 1
    }
    for _, str := range s2_arr {
        counter[str] += 1
    }

    res := make([]string, 0, len(s1_arr) + len(s2_arr))
    for str, count := range counter {
        if count == 1 {
            res = append(res, str)
        }
    }

    return res
}