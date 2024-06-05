/*
Runtime 2 ms / Beats 84.09%
Memory 3.00 MB / Beats 88.64%
*/

func commonChars(words []string) []string {
    res := make([]int, 26)
    for i := 0; i < 26; i++ {
        res[i] = math.MaxInt32
    }
    
    for i := 0; i < len(words); i++ {
        count := make([]int, 26)
		for _, char := range words[i] {
			count[char-'a']++
		}
        for i := 0; i < 26; i++ {
			res[i] = min(res[i], count[i])
		}
    }

    res_arr := make([]string, 0)
    for i := 0; i < 26; i++ {
        for res[i] != 0 {
            res_arr = append(res_arr, string('a'+i))
            res[i]--
        }
    }

    return res_arr
}