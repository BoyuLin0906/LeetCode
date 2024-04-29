/*
Runtime 85 ms / Beats 92.31%
Memory 11.98 MB / Beats 7.69%
*/

func minOperations(nums []int, k int) int {
    xor_num := 0
    for _, num := range nums {
        xor_num ^= num
    }

    count := 0
    xor_num = xor_num ^ k
    for xor_num != 0 {
        if xor_num % 2 == 1 {
            count++
        }
        xor_num = xor_num >> 1
    }

    return count
}