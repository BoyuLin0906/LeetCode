/*
Runtime 70 ms / Beats 66.32%
Memory 14.05 MB / Beats 51.03%
*/

func rangeSum(nums []int, n int, left int, right int) int {
    subarray_sum := make([]int, 1)
    for i := 0; i < n; i++ {
        sum := 0
        for j := i; j < n; j++ {
            sum += nums[j]
            subarray_sum = append(subarray_sum, sum)
        }
    }
    sort.Ints(subarray_sum)

    res := 0
    for i := left; i <= right; i++ {
        res += subarray_sum[i]
    }

    return res % 1000000007
}