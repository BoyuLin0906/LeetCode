/*
Runtime 19 ms / Beats 95.93%
Memory 7.38 MB / Beats 65.76%
*/


type NumHeap []int
func (h NumHeap) Len() int           { return len(h) }
func (h NumHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h NumHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *NumHeap) Push(x any) {
	*h = append(*h, x.(int))
}
func (h *NumHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type KthLargest struct {
    NumHeapQueue *NumHeap
    Largest      int
}

func Constructor(k int, nums []int) KthLargest {
    nums_len := len(nums)
    h := &NumHeap{}
    heap.Init(h)
    k_obj := KthLargest{NumHeapQueue: h, Largest: k}
    
    for i := 0; i < nums_len; i++ {  
        k_obj.Add(nums[i])
    }

    return k_obj
}


func (this *KthLargest) Add(val int) int {
    queue := this.NumHeapQueue
    if len(*queue) < this.Largest || val > (*queue)[0] {
        heap.Push(queue, val)
        if len(*queue) > this.Largest {
            heap.Pop(queue)
        }
    }
    return (*queue)[0]
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */