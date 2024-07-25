/*
Runtime 110 ms / Beats 90.62%
Memory 7.46 MB / Beats 96.78%
*/

func maxHeapify(arr []int, idx int, length int) {
	left := idx*2 + 1
	right := idx*2 + 2

	largest := idx
	if left <= length && arr[idx] < arr[left] {
		largest = left
	}

	if right <= length && arr[largest] < arr[right] {
		largest = right
	}

	if idx != largest {
		swap(&arr[idx], &arr[largest])
		maxHeapify(arr, largest, length)
	}
}

func buildMaxHeap(arr []int) {
	for i := len(arr)/2 - 1; i > -1; i-- {
		maxHeapify(arr, i, len(arr)-1)
	}
}

func heapSort(arr []int) {
	buildMaxHeap(arr)
	size := len(arr) - 1
	for i := len(arr) - 1; i >= 1; i-- {
		size -= 1
		swap(&arr[0], &arr[i])
		maxHeapify(arr, 0, size)
	}
}

func swap(a *int, b *int) {
	*a, *b = *b, *a
}

func sortArray(nums []int) []int {
    heapSort(nums)
    return nums
}