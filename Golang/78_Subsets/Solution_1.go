/*
Runtime 0 ms / Beats 100.00%
Memory 2.92 MB / Beats 9.34%
*/


func subsets(nums []int) [][]int {
    sub_num := make([]int, 0)
    return helper(nums, 0, sub_num)
}

func helper(nums []int, index int, sub_num []int) [][]int {
    if index == len(nums) {
        return [][]int{sub_num}
    }
    with_element := append(sub_num, nums[index])
    with_element_nums := helper(nums, index+1, with_element)

    without_element := make([]int, len(sub_num))
    copy(without_element, sub_num)
    without_element_nums := helper(nums, index+1, without_element)

    merge_nums := append(with_element_nums, without_element_nums...)
    return merge_nums
}