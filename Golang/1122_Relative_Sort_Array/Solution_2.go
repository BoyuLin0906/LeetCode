/*
Runtime 2 ms / Beats 76.92%
Memory 2.90 MB / Beats 5.13%
*/

func relativeSortArray(arr1 []int, arr2 []int) []int {
    max_num := slices.Max(arr1)
    counter := make(map[int]int, max_num+1)

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
    }

    for i := 0; i < max_num+1; i++ {
        for counter[i] > 0 {
            res[idx] = i
            idx += 1
            counter[i] -= 1
        }
    }

    return res
}