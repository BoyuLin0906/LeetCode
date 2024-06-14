/*
Runtime 111 ms / Beats 88.89%
Memory 7.80 MB / Beats 77.78%
*/

func minIncrementForUnique(nums []int) int {
    sort.Ints(nums)
    moves := 0

    for i := 1; i < len(nums); i++ {
        if nums[i] <= nums[i-1] {
            inc_val := nums[i-1] - nums[i] + 1
            moves += inc_val
            nums[i] = nums[i-1] + 1
        }
    }
    
    return moves
}