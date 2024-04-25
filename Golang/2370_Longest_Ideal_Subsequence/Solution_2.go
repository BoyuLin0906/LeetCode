/*
Runtime 107 ms / Beats 50.00%
Memory 5.46 MB / Beats 50.00%
*/

func longestIdealString(s string, k int) int {
    
    dp := make(map[int]int, 26)
    res := 0
    for _, r := range(s) {
        alphabet_num := int(r)
        left := alphabet_num - k
        right := alphabet_num + k
        cur := 1
        for j := max(97, left); j <= min(122, right); j ++ {
            cur = max(cur, dp[j]+1)
        }
        dp[alphabet_num] = cur
        res = max(cur, res)
    }

    return res
}