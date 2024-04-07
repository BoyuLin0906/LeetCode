/*
Runtime 14 ms / Beats 99.73%
Memory 8.29 MB / Beats 7.36%
*/

func sortedSquares(nums []int) []int {
    nums_len := len(nums)
    left_index, right_index := 0, nums_len-1

    for i := 0; i < nums_len; i++ {
        nums[i] = nums[i] * nums[i]
    }
    
    res := make([]int, nums_len)
    index := nums_len-1
    for left_index <= right_index && index > -1 {
        if nums[left_index] >= nums[right_index] {
            res[index] = nums[left_index]
            left_index++
        } else {
            res[index] = nums[right_index]
            right_index--
        }
        index--
    }
    return res
}