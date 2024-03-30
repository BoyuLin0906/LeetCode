func maxSubarrayLength(nums []int, k int) int {
    /*
    Runtime 179 ms / Beats 82.15%
    Memory 10.62 MB / Beats 90.60%

    Counting and Sliding Window
    */
    pointer_start, pointer_end, res := 0, 0, 1
    nums_len := len(nums)
    counter := make(map[int]int)
    
    for pointer_end < nums_len {
        if counter[nums[pointer_end]] + 1 > k {
            counter[nums[pointer_start]] -= 1
            pointer_start += 1
            continue
        }
        counter[nums[pointer_end]] += 1
        res = max(res, pointer_end - pointer_start + 1)
        pointer_end += 1
    }

    return res
}