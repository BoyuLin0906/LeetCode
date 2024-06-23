/*
Runtime 43 ms / Beats 100.00%
Memory 7.66 MB / Beats 96.00%
*/

func longestSubarray(nums []int, limit int) int {
    
    max_based_queue := make([]int, 0, len(nums))
    min_based_queue := make([]int, 0, len(nums))
    left_idx := 0
    res := 0

    for right_idx := 0; right_idx < len(nums); right_idx++{
        
        for len(max_based_queue) > 0 && max_based_queue[len(max_based_queue)-1] < nums[right_idx] {
            max_based_queue = max_based_queue[:len(max_based_queue)-1]
        }
        max_based_queue = append(max_based_queue, nums[right_idx])

        for len(min_based_queue) > 0 && min_based_queue[len(min_based_queue)-1] > nums[right_idx] {
            min_based_queue = min_based_queue[:len(min_based_queue)-1]
        }
        min_based_queue = append(min_based_queue, nums[right_idx])
        
        if max_based_queue[0] - min_based_queue[0] > limit {

            if max_based_queue[0] == nums[left_idx] {
                max_based_queue = max_based_queue[1:]
            }
            if min_based_queue[0] == nums[left_idx] {
                min_based_queue = min_based_queue[1:]
            }
            left_idx += 1
        }
        res = max(res, right_idx - left_idx + 1)
    }

    return res
}