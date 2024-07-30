/*
Runtime 29 ms / Beats 66.67%
Memory 8.58 MB / Beats 16.67%
*/

func minimumDeletions(s string) int {
    s_len := len(s)
    dp := make([]int, s_len + 1)
    b_count := 0

    for i := 0; i < s_len; i++ {
        if s[i] == 'b' {
            dp[i+1] = dp[i]
            b_count++
        } else {
            dp[i+1] = min(dp[i]+1, b_count)
        }
    }

    return dp[s_len]
}