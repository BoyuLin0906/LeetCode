/*
Runtime 74 ms / Beats 100.00%
Memory 8.23 MB / Beats 87.50%
*/

func minSwaps(nums []int) int {
    
    nums_len := len(nums)
    total_one := 0
    for _, num := range nums {
        total_one += num
    }

    swap := math.MaxInt
    cur_total_one := 0
    for i := 0; i < nums_len + total_one; i++ {
        if i >= total_one {
            cur_total_one -= nums[(i-total_one) % nums_len]
        }
        cur_total_one += nums[i % nums_len]
        swap = min(swap, total_one - cur_total_one)
    }

    return swap
}