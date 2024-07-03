/*
Runtime 57 ms / Beats 90.00%
Memory 7.85 MB / Beats 46.67%
*/

func minDifference(nums []int) int {
    if len(nums) <= 4 {
        return 0
    } 

    sort.Ints(nums)
    min_diff := math.MaxInt
    for left_idx := 0; left_idx < 4; left_idx++ {
        right_idx := len(nums) - 4 + left_idx
        min_diff = min(min_diff, nums[right_idx]-nums[left_idx])

    }

    return min_diff
}