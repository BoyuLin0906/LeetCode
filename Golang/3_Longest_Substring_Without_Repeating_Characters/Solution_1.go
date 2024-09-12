/*
Runtime 7 ms / Beats 87.92%
Memory 3.37 MB / Beats 58.02%
*/

func lengthOfLongestSubstring(s string) int {
    table := make(map[rune]int, 0)
    res := 0
    count := 0
    prev_idx := 0
    for _, char := range s {
        table[char] += 1 
        count++

        for table[char] > 1 {
            table[rune(s[prev_idx])] -= 1 
            prev_idx++
            count--
        }
        res = max(res, count)
    }

    return res
}