/*
Runtime 4 ms / Beats 87.64%
Memory 4.76 MB / Beats 49.43%
*/

func canBeEqual(target []int, arr []int) bool {
    if len(target) != len(arr) {
        return false
    }

    table := make(map[int]int, len(arr))
    for i := 0; i < len(arr); i++ {
        table[arr[i]] += 1
        table[target[i]] -= 1
    }

    for _, val := range table {
        if val != 0 {
            return false
        }
    }

    return true
}