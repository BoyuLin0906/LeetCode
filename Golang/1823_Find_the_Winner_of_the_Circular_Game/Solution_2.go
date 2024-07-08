/*
Runtime 1 ms / Beats 92.86%
Memory 2.18 MB / Beats 100.00%
*/

// Josephus Problem
func findTheWinner(n int, k int) int {
    
    res := 0
    for i := 2; i <= n; i++ {
        res = (res + k) % i
    }
    return res+1
}