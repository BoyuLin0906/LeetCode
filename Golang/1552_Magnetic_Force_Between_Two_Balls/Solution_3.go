/*
Runtime 109 ms / Beats 73.68%
Memory 9.26 MB / Beats 26.32%
*/

func maxDistance(position []int, m int) int {
    sort.Ints(position)
    start := 1
    end := position[len(position)-1]

    for start <= end {
        // (start + end)/2 -> may overflow
        // end - (end - start)/2 -> better to use this method
        mid := end - (end - start)/2
        if helper(position, m, mid) {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    return end
}

func helper(position []int, m int, force int) bool {
    prev_pos := position[0]
    count := 1
    for i := 1; i < len(position); i++ {
        if position[i] - prev_pos >= force {
            count += 1
            prev_pos = position[i]
        }
        if count == m {
            return true
        }
    }
    return false
}