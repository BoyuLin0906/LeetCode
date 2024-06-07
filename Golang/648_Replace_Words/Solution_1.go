/*
Runtime 164 ms / Beats 13.89%
Memory 8.05 MB / Beats 100.00%
*/


func replaceWords(dictionary []string, sentence string) string {
    sentence_slice := strings.Split(sentence, " ")
    s_len := len(sentence_slice)

    sort.Slice(dictionary, func(i, j int) bool {
		if len(dictionary[i]) != len(dictionary[j]) {
			return len(dictionary[i]) < len(dictionary[j])
		}
		return dictionary[i] < dictionary[j]
	})

    for i := 0; i < s_len; i++ {
        for _, word := range dictionary{
            is_ok := true
            if len(sentence_slice[i]) < len(word) {
                continue
            }
            for j, k := 0, 0; j < len(word) && k < len(sentence_slice[i]); j, k = j+1, k+1 {
                if word[j] != sentence_slice[i][k] {
                    is_ok = false
                }
            }
            if is_ok {
                sentence_slice[i] = word
                break
            }
        }
    }

    return strings.Join(sentence_slice[:], " ")
}