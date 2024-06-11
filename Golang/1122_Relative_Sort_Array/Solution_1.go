/*
Runtime 1 ms / Beats 82.05%
Memory 2.60 MB / Beats 51.28%
*/

func relativeSortArray(arr1 []int, arr2 []int) []int {
    counter := make(map[int]int)

    for _, val := range arr1 {
        counter[val] += 1
    } 

    res := make([]int, len(arr1))
    idx := 0
    for _, val := range arr2 {
        for counter[val] > 0 {
            res[idx] = val
            idx += 1
            counter[val] -= 1
        }
        delete(counter, val);
    }

    keys := make([]int, 0, len(counter))
    for key, _ := range counter {
        keys = append(keys, key)
    }
    sort.Ints(keys)

    for _, key := range keys {
        for counter[key] > 0 {
            res[idx] = key
            idx += 1
            counter[key] -= 1
        }
    }

    return res
}