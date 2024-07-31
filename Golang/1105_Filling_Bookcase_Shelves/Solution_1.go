/*
Runtime 3 ms / Beats 66.67%
Memory 2.73 MB / Beats 58.33%
*/

func minHeightShelves(books [][]int, shelfWidth int) int {
    dp := make([]int, len(books)+1)

    for i := 1; i <= len(books); i++ {
        total_width := 0
        max_height := 0
        dp[i] = math.MaxInt
        
        for j := i; j >= 1; j-- {
            max_height = max(max_height, books[j-1][1])
            total_width += books[j-1][0]
            if total_width > shelfWidth {
                break
            }
            dp[i] = min(dp[i], dp[j-1] + max_height)
        }
    }

    return dp[len(books)]
}