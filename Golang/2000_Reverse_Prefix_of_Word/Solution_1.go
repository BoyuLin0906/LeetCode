/*
Runtime 0 ms / Beats 100.00%
Memory 5.38 MB / Beats 5.13%
*/


func reversePrefix(word string, ch byte) string {

    index := -1
    for i := 0; i < len(word); i++ {
        if word[i] == ch {
            index = i
            break
        }
    }

    if index == -1 {
        return word
    }

    res := ""
    for i := 0; i < len(word); i++ {
        if i <= index {
            res = string(word[i]) + res
        } else {
            res = res + string(word[i])
        }
    } 

    return res
}