/*
Runtime 1 ms / Beats 92.86%
Memory 2.18 MB / Beats 66.67%
*/


func subsetXORSum(nums []int) int {
    return helper(nums, 0, 0)
}

func helper(nums []int, index int, curr_xor_val int) int {
    if index == len(nums) {
        return curr_xor_val
    }
    with_index := helper(nums, index+1, curr_xor_val^nums[index])
    without_index := helper(nums, index+1, curr_xor_val)
    return with_index + without_index
}