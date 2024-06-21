/*
Runtime 96 ms / Beats 100.00%
Memory 8.11 MB / Beats 84.21%
*/

func maxDistance(position []int, m int) int {
    sort.Ints(position)
    start := 1
    end := position[len(position)-1]

    for start <= end {
        mid := (start + end) / 2
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