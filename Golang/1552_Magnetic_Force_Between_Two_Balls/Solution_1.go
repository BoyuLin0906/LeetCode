/*
Runtime 111 ms / Beats 63.16%
Memory 8.92 MB / Beats 31.58%
*/

func maxDistance(position []int, m int) int {
    start := 1
    end := slices.Max(position)
    sort.Ints(position)

    for start <= end {
        mid := (start + end) / 2
        set_m := helper(position, m, mid)

        if set_m <= 0 {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    return start - 1
}

func helper(position []int, m int, force int) int {
    prev_pos := position[0]
    m -= 1
    for i := 1; i < len(position); i++ {
        if position[i] - prev_pos >= force {
            m -= 1
            prev_pos = position[i]
        }
    }
    return m
}