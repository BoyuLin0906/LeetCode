/*
Runtime 9 ms / Beats 28.13%
Memory 3.66 MB / Beats 99.51%
*/

func canBeEqual(target []int, arr []int) bool {
    sort.Ints(target)
	sort.Ints(arr)
    return reflect.DeepEqual(target, arr)
}