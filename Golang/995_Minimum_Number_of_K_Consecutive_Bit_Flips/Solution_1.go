/*
Runtime 110 ms / Beats 66.67%
Memory 9.37 MB / Beats 33.33%
*/

func minKBitFlips(nums []int, k int) int {
    count := 0
    flip := 0
    diff := make([]int, len(nums)+k)

    for i := 0; i < len(nums); i++ {
        flip += diff[i]

        if (flip + nums[i]) % 2 == 1 {
            continue
        }

        if ( i+k-1 >= len(nums) ) {
            return -1
        }

        flip += 1
        diff[i+k] -= 1
        count += 1
    }

    return count
}