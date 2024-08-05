/*
Runtime 3 ms / Beats 91.43%
Memory 5.62 MB / Beats 80.00%
*/
func kthDistinct(arr []string, k int) string {
    table := make(map[string]int)
    for _, s := range arr {
        table[s] += 1 
    }

    k_count := 0
    res := ""
    for _, s := range arr {
        count := table[s]
        if count != 1 {
            continue
        }

        k_count += 1
        if k_count == k {
            res = s
            break
        }
    }

    return res
}