/*
Runtime 0 ms / Beats 100.00%
Memory 2.43 MB / Beats 95.56%
*/

func rangeSum(nums []int, n int, left int, right int) int {
	min_sum := math.MaxInt
	max_sum := 0
	mod := 1000000007

	for _, num := range nums {
		if num < min_sum {
			min_sum = num
		}
		max_sum += num
	}

	// left-1 -> left to right -> e.g. left=2, right=5 -> 2-5 -> sum(5) - sum(1) = sum(5-2) 
	res := (sum_of_first_k(nums, n, right, min_sum, max_sum) - sum_of_first_k(nums, n, left-1, min_sum, max_sum)) % mod
	return res
}

func count_and_sum(nums []int, n int, target int) (int, int) {
	count := 0
	cur_sum := 0
	total_sum := 0
	window_sum := 0
	i := 0
	for j := 0; j < n; j++ {
		cur_sum += nums[j]
		window_sum += nums[j] * (j - i + 1)
		for cur_sum > target {
			window_sum -= cur_sum
			cur_sum -= nums[i]
			i++
		}
		count += (j - i + 1)
		total_sum += window_sum
	}
	return count, total_sum
}

func sum_of_first_k(nums []int, n int, k int, left int, right int) int {
	for left <= right {
		middle := left + (right-left)/2
		count, _ := count_and_sum(nums, n, middle)
		if count >= k {
			right = middle - 1
		} else {
			left = middle + 1
		}
	}
	count, sum := count_and_sum(nums, n, left)
	// There can be more subarrays with the same sum of left
	// 1 2 3 '3' ... 
	return sum - left * (count-k)
}