/*
Runtime 43 ms / Beats 76.19%
Memory 8.82 MB /Beats 38.10%
*/

func xorQueries(arr []int, queries [][]int) []int {
    prefix_xor_sum := make([]int, len(arr)+1)
    prefix_xor_sum[0] = 0

    for i := 0; i < len(arr); i++ {
        prefix_xor_sum[i+1] = prefix_xor_sum[i] ^ arr[i]
    }

    res := make([]int, len(queries))
    for i := 0; i < len(queries); i++ {
        query := queries[i]
        res[i] = prefix_xor_sum[query[1]+1] ^ prefix_xor_sum[query[0]]
    }

    return res
}