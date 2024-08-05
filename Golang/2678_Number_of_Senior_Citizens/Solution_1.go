/*
Runtime 0 ms / Beats 100.00%
Memory 3.20 MB / Beats 76.74%
*/

func countSeniors(details []string) int {
    count := 0
    for _, detail := range details {
        age, _ := strconv.Atoi(detail[11:13])
        if age > 60 {
            count++
        }
    }

    return count
}