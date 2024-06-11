/*
Runtime 2 ms / Beats 76.92%
Memory 2.48 MB / Beats 89.74%
*/

func relativeSortArray(arr1 []int, arr2 []int) []int {
    
    arr2_dict := make(map[int]int, len(arr2))
    for idx, val := range arr2 {
        arr2_dict[val] = idx
    } 

    sort.Slice(arr1, func(i, j int) bool {
        arr2_idx_1, ok_1 := arr2_dict[arr1[i]]
        arr2_idx_2, ok_2 := arr2_dict[arr1[j]]

        if !ok_1 && !ok_2 {
            return arr1[i] < arr1[j]
        }

        if ok_1 && ok_2 {
            return arr2_idx_1 < arr2_idx_2
        }

        if ok_1 {
            return true
        }
        return false
    })

    return arr1
}