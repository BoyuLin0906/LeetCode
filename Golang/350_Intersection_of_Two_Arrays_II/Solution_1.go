/*
Runtime 0 ms / Beats 100.00%
Memory 3.01 MB / Beats 70.08%
*/

func intersect(nums1 []int, nums2 []int) []int {
 
    tables := make(map[int]int, len(nums1))
    for _, num := range nums1 {
        tables[num] += 1
    }

    res := make([]int, 0, len(nums2))
    for _, num := range nums2 {
        if tables[num] > 0 {
            res = append(res, num)
            tables[num] -= 1
        }
    }

    return res
}