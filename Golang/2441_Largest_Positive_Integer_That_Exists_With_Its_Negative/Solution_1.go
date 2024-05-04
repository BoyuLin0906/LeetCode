/*
Runtime 9 ms / Beats 96.15%
Memory 5.07 MB / Beats 92.31%
*/

func findMaxK(nums []int) int {
    sort.Ints(nums)
    left := 0
    right := len(nums)-1

    for left < right {
        if -nums[left] == nums[right] {
            return nums[right]
        }else if -nums[left] > nums[right] {
            left++
        }else {
            right--
        }
    }

    return -1
}