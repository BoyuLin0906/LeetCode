/*
Runtime 102 ms / Beats 100.00%
Memory 8.25 MB / Beats 33.33%
*/

func minKBitFlips(nums []int, k int) int {
    count := 0
    flip := 0

    for i := 0; i < len(nums); i++ {
        if i >= k && nums[i-k] == 2{
            flip -= 1
        }

        if (flip + nums[i]) % 2 == 1 {
            continue
        }

        if ( i+k-1 >= len(nums) ) {
            return -1
        }

        flip += 1
        nums[i] = 2 
        count += 1
    }

    return count
}