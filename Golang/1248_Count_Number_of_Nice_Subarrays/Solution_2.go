/*
Runtime 107 ms / Beats 38.46%
Memory 8.25 MB / Beats 38.46%
*/

func numberOfSubarrays(nums []int, k int) int {

    curr_sum := 0
    prefix_sum := make(map[int]int, len(nums))
    prefix_sum[0] = 1
    res := 0

    for i := 0; i < len(nums); i++ {
        curr_sum += nums[i] % 2
        
        val, is_ok := prefix_sum[curr_sum - k]
        if is_ok {
            res += val
        }
        prefix_sum[curr_sum] += 1
    }

    return res 
}