/*
Runtime 570 ms / Beats 62.35%
Memory 96.10 MB / Beats 13.24%
*/

type Fraction struct {
    TopNum int
    BottomNum int
    Val float64
}

// official
type IntHeap []Fraction
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i].Val < h[j].Val }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(Fraction))
}
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
    arr_len := len(arr)
    h := &IntHeap{}
    heap.Init(h)

    for i := 0; i < arr_len-1; i++ {
        for j := i+1; j < arr_len; j++ {
            f := Fraction{TopNum: arr[i], BottomNum: arr[j], Val: float64(arr[i])/float64(arr[j])}
            heap.Push(h, f)
        }
    }

    top_num, bottom_num := 0, 0
    for k > 0 {
        k--
        f := heap.Pop(h)
        top_num = f.(Fraction).TopNum
        bottom_num = f.(Fraction).BottomNum
    }

    return []int{top_num, bottom_num}
}