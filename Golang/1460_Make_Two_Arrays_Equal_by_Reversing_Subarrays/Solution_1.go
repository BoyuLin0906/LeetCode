/*
Runtime 8 ms / Beats 46.67%
Memory 4.53 MB / Beats 51.54%
*/

func canBeEqual(target []int, arr []int) bool {
    if len(target) != len(arr) {
        return false
    }

    table := make(map[int]int, len(arr))
    for _, val := range arr {
        table[val] += 1
    }

    for _, val := range target {
        if _, ok := table[val]; !ok {
            return false
        }
        table[val] -= 1
        if  table[val] == 0 {
            delete(table, val)
        }
    }

    return true
}