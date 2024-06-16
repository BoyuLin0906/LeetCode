/*
Runtime 4 ms / Beats 70.00%
Memory 3.92 MB / Beats 70.00%
*/

func minPatches(nums []int, n int) int {
    miss_val := 1
    idx := 0
    org_nums_len := len(nums) 
    
    for miss_val <= n {
        if idx >= len(nums) || miss_val < nums[idx] {
            tmp := make([]int, len(nums[idx:]))
            copy(tmp, nums[idx:])
            nums = append(nums[:idx], miss_val)
            nums = append(nums, tmp...)
        }
        miss_val += nums[idx]
        idx += 1
    }
    return len(nums) - org_nums_len
}