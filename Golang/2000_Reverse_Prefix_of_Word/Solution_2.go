/*
Runtime 1 ms / Beats 76.52%
Memory 2.31 MB / Beats 28.70%
*/

func reversePrefix(word string, ch byte) string {

    res := ""
    for i := 0; i < len(word); i++ {
        res = string(word[i]) + res
        if word[i] == ch {
           return res + word[i+1:]
        }
    }

    return word
}