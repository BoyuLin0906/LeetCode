/*
Runtime 0 ms / Beats 100.00%
Memory 2.73 MB / Beats 13.33%
*/

func threeConsecutiveOdds(arr []int) bool {
    count := 0
    for _, val := range arr {
        if val % 2 == 1 {
            count += 1
        } else {
            count = 0
        }

        if count == 3 {
            return true
        }
    }

    return false
}