/*
Runtime 533 ms / Beats 50.00%
Memory 10.56 MB / Beats 50.00%
*/


func longestIdealString(s string, k int) int {
    alphabet := make(map[int]int, 26)
    for i := 97; i <= 122; i++ {
        alphabet[i] = -1
    }

    dp := make(map[int]int, len(s))
    res := 0
    for i, r := range(s) {
        alphabet_num := int(r)
        left := alphabet_num - k
        right := alphabet_num + k
        for j := max(97, left); j <= min(122, right); j ++ {
            prev_alphabet := alphabet[j]
            if prev_alphabet != -1 {
                dp[i] = max(dp[i], dp[prev_alphabet] + 1)
            }
        }
        alphabet[alphabet_num] = i
        res = max(dp[i]+1, res)
    }

    return res
}