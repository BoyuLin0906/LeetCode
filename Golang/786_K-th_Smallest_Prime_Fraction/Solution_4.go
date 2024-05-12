func kthSmallestPrimeFraction(arr []int, k int) []int {
	left_val, right_val := 0.00, 1.00
	arr_len := len(arr)
	var res []int

	for left_val < right_val {
		mid_val := (left_val + right_val) / 2
		count := 0
		j := 1
		max_frac := 0.0
		top_idx := 0
		bottom_idx := 0
		for i := 0; i < arr_len; i ++ {
			for j < arr_len && float64(arr[i]) / float64(arr[j]) >= mid_val {
				j++
			}

			count += (arr_len - j)
			if j < arr_len && max_frac < float64(arr[i])/float64(arr[j]) {
				max_frac = float64(arr[i]) / float64(arr[j])
				top_idx, bottom_idx = i, j
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