/*
Runtime 106 ms / Beats 16.00%
Memory 8.44 MB / Beats 68.00%
*/

func longestSubarray(nums []int, limit int) int {
    
    left_idx := 0
    right_idx := 0
    max_idx := 0
    min_idx := 0
    res := 0

    for right_idx < len(nums) {
        if left_idx == right_idx {
            right_idx += 1
            continue
        }

        if nums[max_idx] <= nums[right_idx] {
            max_idx = right_idx
        }
        if nums[min_idx] >= nums[right_idx] {
            min_idx = right_idx
        }

        if nums[max_idx] - nums[min_idx] <= limit {
            right_idx += 1
            continue
        }

        res = max(res, right_idx - left_idx)
        left_idx = min(max_idx, min_idx) + 1
        max_idx, min_idx = left_idx, left_idx
        right_idx = left_idx + 1
    }

    return max(res, right_idx - left_idx)
}