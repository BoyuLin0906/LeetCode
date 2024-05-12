/*
Runtime 269 ms / Beats 77.94%
Memory 17.26 MB / Beats 74.71%
*/

type Fraction struct {
    TopNumIdx int
    BottomIdx int
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
        f := Fraction{i, arr_len-1, float64(arr[i])/float64(arr[arr_len-1])}
        heap.Push(h, f)
    }

    top_num, bottom_num := 0, 0
    for {
        k--
        f := heap.Pop(h)

        topIdx := f.(Fraction).TopNumIdx
        buttomIdx := f.(Fraction).BottomIdx
        if k == 0 {
            top_num = arr[topIdx]
            bottom_num = arr[buttomIdx]
            break
        }

        buttomIdx = buttomIdx - 1
        if topIdx < buttomIdx {
            next_f := Fraction{topIdx, buttomIdx, float64(arr[topIdx])/float64(arr[buttomIdx])}
            heap.Push(h, next_f)
        }
    }
       
    return []int{top_num, bottom_num}
}