/*
Runtime 1 ms / Beats 74.46%
Memory 2.34 MB / Beats 84.24%
*/

// implement counting sort
func heightChecker(heights []int) int {

    heights_count := make([]int, 101)
    for i := 0; i < len(heights); i++ {
        heights_count[heights[i]] += 1
    }

    count := 0
    h_idx := 0
    for i := 1; i < 101 && h_idx < len(heights); i++ {
        for j := 0; j < heights_count[i]; j++ {
            if heights[h_idx] != i {
                count += 1
            }
            h_idx += 1
        }
    }

    return count
}