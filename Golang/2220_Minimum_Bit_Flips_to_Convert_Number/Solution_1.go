/*
Runtime 2 ms / Beats 51.16%
Memory 2.19 MB / Beats 95.35%
*/

func minBitFlips(start int, goal int) int {

    mask := 1
    count := 0

    for start > 0 || goal > 0 {
        if start & mask != goal & mask {
            count += 1
        }
        start = start >> 1
        goal = goal >> 1
    }

    return count
}