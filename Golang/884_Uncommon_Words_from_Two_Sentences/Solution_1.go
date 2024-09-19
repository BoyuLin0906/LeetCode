/*
Runtime 1 ms / Beats 77.91%
Memory 2.50 MB / Beats 77.16%
*/

func uncommonFromSentences(s1 string, s2 string) []string {
    s1_arr := strings.Split(s1, " ")
    s2_arr := strings.Split(s2, " ")

    s1_counter := make(map[string]int, 0)
    s2_counter := make(map[string]int, 0)

    for _, str := range s1_arr {
        s1_counter[str] += 1
    }
    for _, str := range s2_arr {
        s2_counter[str] += 1
    } 

    res := make([]string, 0, len(s1_arr) + len(s2_arr))
    for str, s1_count := range s1_counter {
        if s1_count != 1 {
            continue
        }
        if _, is_ok := s2_counter[str]; !is_ok {
            res = append(res, str)
        }
    }

    for str, s2_count := range s2_counter {
        if s2_count != 1 {
            continue
        }
        if _, is_ok := s1_counter[str]; !is_ok {
            res = append(res, str)
        }
    }

    return res
}