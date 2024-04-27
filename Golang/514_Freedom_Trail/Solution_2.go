/*
Runtime 129 ms / Beats 16.67%
Memory 7.42 MB / Beats 16.67%

Need to optimize
1. Heap Algorithm
2. queue
*/

type queueObj struct {
    key_idx int
    table_idx int
    sum int
}

type MaxHeap struct {
    slice    []*queueObj
    heapSize int
}

func BuildMaxHeap(slice []*queueObj) MaxHeap {
    h := MaxHeap{slice: slice, heapSize: len(slice)}
    for i := len(slice) / 2; i >= 0; i-- {
        h.MaxHeapify(i)
    }
    return h
}

func (h MaxHeap) MaxHeapify(i int) {
    l, r := 2*i+1, 2*i+2
    max := i

    if l < h.size() && h.slice[l].sum > h.slice[max].sum {
        max = l
    }
    if r < h.size() && h.slice[r].sum > h.slice[max].sum {
        max = r
    }
    if max != i {
        h.slice[i], h.slice[max] = h.slice[max], h.slice[i]
        h.MaxHeapify(max)
    }
}

func (h MaxHeap) size() int { return h.heapSize } // ???

func heapSort(slice []*queueObj) {
    h := BuildMaxHeap(slice)
    for i := len(h.slice) - 1; i >= 1; i-- {
        h.slice[0], h.slice[i] = h.slice[i], h.slice[0]
        h.heapSize--
        h.MaxHeapify(0)
    }
}

func findRotateSteps(ring string, key string) int {
    ring_len := len(ring)
    key_len := len(key)
    
    step_tables := make([][]bool, ring_len)
    for i := 0; i < ring_len; i++ {
        step_tables[i] = make([]bool, key_len)
        for j := 0; j < key_len; j++ {
            step_tables[i][j] = false
        }
    }

    index_mapping := make(map[byte][]int)
    for i := 0; i < ring_len; i++ {
        index_mapping[ring[i]] = append(index_mapping[ring[i]], i)
    } 
    res := math.MaxInt64
    queue := make([]*queueObj, 0)
    queue = append(queue, &queueObj{key_idx: 0, table_idx: 0, sum: 0})

    for len(queue) > 0 {
        obj := queue[0]
        queue = queue[1:]
        
        k_idx := obj.key_idx
        t_idx := obj.table_idx
        sum := obj.sum
        

        if k_idx == key_len {
           res = min(sum, res)
           continue
        }

        if step_tables[t_idx][k_idx] {
            continue
        }
        step_tables[t_idx][k_idx] = true

        next_indexes := index_mapping[key[k_idx]]
        for _, idx := range next_indexes {
            diff := t_idx - idx
            if diff < 0 {
                diff = -diff
            }
            tmp_sum := sum + min(diff, ring_len - diff)
            queue = append(queue, &queueObj{key_idx: k_idx + 1, table_idx: idx, sum: tmp_sum})  
        }
        heapSort(queue)
    }

    return res + key_len
}