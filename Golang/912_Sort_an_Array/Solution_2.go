/*
Runtime 91 ms / Beats 97.86%
Memory 7.92 MB / Beats 89.81%
*/

func CountingSort(arr []int) []int {
	max_val := arr[0]
	min_val := arr[0]

	for i := 1; i < len(arr); i++ {
		if arr[i] > max_val {
			max_val = arr[i]
		}
		if arr[i] < min_val {
			min_val = arr[i]
		}
	} 

	// for negative value
	offset := 0
	if min_val < 0 {
		offset = -min_val
	}

	count := make([]int, max_val+offset+1)
	for i := 0; i < len(arr); i++ {
		count[arr[i]+offset] += 1
	}

	for i := 1; i < len(count); i++ {
		count[i] += count[i-1]
	} 

	output_arr := make([]int, len(arr))
	for i := 0; i < len(arr); i++ {
		count[arr[i]+offset] -= 1
		output_arr[count[arr[i]+offset]] = arr[i]
	}

	return output_arr
}

func sortArray(nums []int) []int {
    output_nums := CountingSort(nums)
    return output_nums
}