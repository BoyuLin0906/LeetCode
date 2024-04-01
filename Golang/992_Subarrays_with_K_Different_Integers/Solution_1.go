func subarraysWithKDistinct(nums []int, k int) int {
    /*
    Runtime 53 ms / Beats 83.08%
    Memory 6.76 MB / Beats 87.59%

    Counting and Sliding Window with three pointers
    */
    near_left_pointer, far_left_pointer := 0, 0
    nums_len := len(nums)
    counter := make(map[int]int)
    res := 0

    for right_pointer := 0; right_pointer < nums_len; right_pointer++ {
	    counter[nums[right_pointer]] += 1

        for len(counter) > k {
            counter[nums[near_left_pointer]] -= 1
            if counter[nums[near_left_pointer]] == 0 {
                delete(counter, nums[near_left_pointer])
            }
            near_left_pointer += 1
            far_left_pointer = near_left_pointer
        }

        for counter[nums[near_left_pointer]] > 1 {
            counter[nums[near_left_pointer]] -= 1
            near_left_pointer += 1
        }

        if len(counter) == k {
            res += (near_left_pointer - far_left_pointer) + 1
        }
    }

    return res
}