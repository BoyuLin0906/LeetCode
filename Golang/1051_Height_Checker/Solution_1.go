/*
Runtime 2 ms / Beats 65.22%
Memory 2.43 MB / Beats 14.13%
*/

func heightChecker(heights []int) int {
    expected := make([]int, len(heights))
    copy(expected, heights)
    sort.Ints(expected)

    count := 0
    for i := 0; i < len(heights); i ++ {
        if expected[i] != heights[i] {
            count += 1
        }
    }

    return count
}