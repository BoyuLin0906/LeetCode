/*
Runtime 79 ms / Beats 92.31%%
Memory 7.95 MB / Beats 76.92%
*/

func minOperations(nums []int, k int) int {
    xor_num := 0
    for _, num := range nums {
        xor_num ^= num
    }

    count := 0 
    for xor_num != 0 || k != 0 {
        if (xor_num & 1) != (k & 1) {
            count++
        }
        xor_num = xor_num >> 1
        k = k >> 1
    }

    return count
}