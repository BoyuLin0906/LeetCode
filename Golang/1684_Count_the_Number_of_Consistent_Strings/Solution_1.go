/*
Runtime 31 ms / Beats 53.91%
Memory 6.86 MB / Beats 86.72%
*/

func countConsistentStrings(allowed string, words []string) int {
    tables := make(map[rune]bool, 0)
    for _, char := range allowed {
        tables[char] = true
    }

    count := 0
    for _, word := range words {
        is_consistent := true
        for _, char := range word {
            if _, ok := tables[char]; !ok {
                is_consistent = false
                break
            }
        }

        if is_consistent {
            count++
        }
    } 

    return count
}