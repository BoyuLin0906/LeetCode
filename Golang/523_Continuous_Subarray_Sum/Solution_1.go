/*
Runtime 131 ms / Beats 96.81%
Memory 11.42 MB / Beats 90.02%
*/

func checkSubarraySum(nums []int, k int) bool {
    prefix_sum_dict := make(map[int]int, len(nums))
    prefix_sum_dict[0] = -1
    prefix_mod_sum := 0

    for i := 0; i < len(nums); i++ {
        // (prefixSum[j] - prefixSum[i]) % k = 0 -> prefixSum[j] % k = prefixSum[i] % k
        prefix_mod_sum = (prefix_mod_sum + nums[i]) % k
        if val, is_ok := prefix_sum_dict[prefix_mod_sum]; is_ok {
            // at least 2
            if i - val > 1 {
                return true
            }
        }  else {
            prefix_sum_dict[prefix_mod_sum] = i
        }
    }
    return false
}