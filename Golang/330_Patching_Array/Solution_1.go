/*
Runtime 2 ms / Beats 90.00%
Memory 3.15 MB / Beats 70.00%
*/

func minPatches(nums []int, n int) int {
    miss_val := 1
    idx := 0
    count := 0

    for miss_val <= n {
        if idx < len(nums) && nums[idx] <= miss_val {
            miss_val += nums[idx]
            idx += 1
        } else {
            miss_val += miss_val
            count += 1
        }
    }

    return count
}