/*
Runtime 2 ms / Beats 51.16%
Memory 2.22 MB / Beats 6.98%
*/

func minBitFlips(start int, goal int) int {
    count := 0
    diff := start ^ goal

    for diff > 0 {
        if diff & 1 == 1 {
            count += 1
        }
        diff = diff >> 1
    }

    return count
}