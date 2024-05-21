/*
Runtime 0 ms / Beats 100.00%
Memory 2.50 MB / Beats 37.63%
*/


func subsets(nums []int) [][]int {
    res := &[][]int{}
    for k := 0; k < len(nums)+1; k++ {
        backtrack_helper(nums, 0, k, []int{}, res)
    }
    return *res
}

func backtrack_helper(nums []int, first int, index int, cur []int, res *[][]int) {
    if len(cur) == index {
        *res = append(*res, append([]int(nil), cur...))
        return
    }

    for i := first; i < len(nums); i++ {
        cur = append(cur, nums[i])
        backtrack_helper(nums, i+1, index, cur, res) 
        cur = cur[:len(cur)-1]
    }
}