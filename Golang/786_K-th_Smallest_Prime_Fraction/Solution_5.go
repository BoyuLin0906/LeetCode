/*
Runtime 3 ms / Beats 98.53%
Memory 2.60 MB / Beats 91.47%
*/

func kthSmallestPrimeFraction(arr []int, k int) []int {
	left_val, right_val := 0.00, 1.00
	arr_len := len(arr)
	var res []int

	for left_val < right_val {
		mid_val := (left_val + right_val) / 2
		count := 0
		j := arr_len - 1
		max_frac := 0.0
		top_idx := 0
		bottom_idx := 0
		for i := 0; i < arr_len; i ++ {
			for j >= 0 && float64(arr[i]) / float64(arr[arr_len-1-j]) >= mid_val {
				j--
			}
			count += (j + 1)
			if j >= 0 && max_frac < float64(arr[i])/float64(arr[arr_len-1-j]) {
				max_frac = float64(arr[i]) / float64(arr[arr_len-1-j])
				top_idx, bottom_idx = i, arr_len-1-j
			}

		} 

		if count == k {
			res = []int{arr[top_idx], arr[bottom_idx]}
			break
		} 

		if count > k {
			right_val = mid_val
		} else {
			left_val = mid_val + 0.0000000001
		}
	}
	return res
}