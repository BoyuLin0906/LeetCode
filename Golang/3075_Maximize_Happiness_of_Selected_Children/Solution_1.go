/*
Runtime 115 ms / Beats 100.00%
Memory 11.96 MB / Beats 60.51%
*/

func maximumHappinessSum(happiness []int, k int) int64 {
    
    sort.Ints(happiness)
    res := 0
    h_len := len(happiness)-1

    for i := 0; i < k; i++ {
        val := happiness[h_len - i] -i
        if val > 0 {
            res += val
        }   
    }

    return int64(res)
}   