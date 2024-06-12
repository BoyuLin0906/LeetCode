/*
Runtime 1 ms / Beats 77.20%
Memory 2.23 MB / Beats 77.73%
*/

func sortColors(nums []int)  {
    left_ptr := 0
    right_ptr := len(nums) - 1

    for i := 0; i < len(nums); i++ {
        for i >= left_ptr && i <= right_ptr && ( nums[i] == 0 || nums[i] == 2 ) {
            if nums[i] == 0 {
                nums[i], nums[left_ptr] = nums[left_ptr], nums[i]
                left_ptr += 1
            } else {
                nums[i], nums[right_ptr] = nums[right_ptr], nums[i]
                right_ptr -= 1
            }
        }
    }
}