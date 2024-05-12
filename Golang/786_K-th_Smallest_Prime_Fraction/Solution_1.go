/*
Runtime 570 ms / Beats 55.88%
Memory 37.59 MB / Beats 65.00%
*/

type fraction struct {
    top_num int
    bottom_num int
    val float64
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
    arr_len := len(arr)
    fraction_slice := make([]*fraction, 0)

    for i := 0; i < arr_len-1; i++ {
        for j := i+1; j < arr_len; j++ {
            f := &fraction{top_num: arr[i], bottom_num: arr[j], val: float64(arr[i])/float64(arr[j])}
            fraction_slice = append(fraction_slice, f)
        }
    }
    
    sort.Slice(fraction_slice, func(i, j int) bool {
		return fraction_slice[i].val < fraction_slice[j].val
	})

    return []int{fraction_slice[k-1].top_num, fraction_slice[k-1].bottom_num}
}