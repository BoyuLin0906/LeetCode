/*
Runtime 59 ms / Beats 84.63%
Memory 6.92 MB / Beats 90.49%
*/

type SubArray struct {
	Sum int
	Idx int
}

type SubArrayHeap []*SubArray

func (h SubArrayHeap) Len() int           { return len(h) }
func (h SubArrayHeap) Less(i, j int) bool { return h[i].Sum < h[j].Sum }
func (h SubArrayHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *SubArrayHeap) Push(x any) {
	*h = append(*h, x.(*SubArray))
}
func (h *SubArrayHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func rangeSum(nums []int, n int, left int, right int) int {

	h := &SubArrayHeap{}
	heap.Init(h)

	for i := 0; i < n; i++ {
		heap.Push(h, &SubArray{Sum: nums[i], Idx: i})
	}

	res := 0
	mod := 1000000007
	for i := 1; i < right+1; i++ {
		p_sub := heap.Pop(h)
		p_sub_sum := p_sub.(*SubArray).Sum
		p_sub_idx := p_sub.(*SubArray).Idx

		if i >= left {
			res = (res + p_sub_sum) % mod
		}

		if p_sub_idx < n-1 {
			heap.Push(h, &SubArray{Sum: p_sub_sum + nums[p_sub_idx+1], Idx: p_sub_idx + 1})
		}
	}

	return res
}