/*
Runtime 111 ms / Beats 82.35%
Memory 9.19 MB / Beats 17.65%
*/

func beautifulSubsets(nums []int, k int) int {
    sort.Ints(nums)
    res := len(nums)
    for i := 0; i < len(nums); i++ {
        helper(nums, k, i, []int{nums[i]}, &res)
    }
    return res
}

func helper(nums []int, diff int, index int, curr []int, res *int) {
    for i := index+1; i < len(nums); i++ {
        if check(curr, nums[i], diff) {
            *res++
            curr = append(curr, nums[i])
            helper(nums, diff, i, curr, res) 
            curr = curr[:len(curr)-1]
        } 
    }
}

func check(curr []int, value int, diff int) bool {
    for _, num := range curr {
        if value - num == diff {
            return false
        }
    }
    return true
}