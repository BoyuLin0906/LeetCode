/*
Runtime 1 ms / Beats 92.86%
Memory 2.12 MB / Beats 66.67%
*/

func subsetXORSum(nums []int) int {
    res := 0

    for _, num := range(nums) {
        res = res | num
    }

    return res << (len(nums) -1) 
}