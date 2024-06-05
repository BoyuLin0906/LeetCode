/*
Runtime 3 ms / Beats 72.73%
Memory 4.23 MB / Beats 28.41%
*/

func commonChars(words []string) []string {
    w_len := len(words)
    res := make([]string, 0)

    first_words_len := len(words[0])
    for j := 0; j < first_words_len; j ++ {
        count := 0
        for i := 1; i < w_len; i++ {
            for k := 0; k < len(words[i]); k++ {
                if words[0][j] == words[i][k] {
                    count++
                    break
                }
            }
        }
        if count == w_len - 1 {
            res = append(res, string(words[0][j]))
            for i := 1; i < w_len; i++ {
                words[i] = strings.Replace(words[i], string(words[0][j]), "", 1)
            }
        }
    }

    return res
}