/*
Runtime 1 ms / Beats 79.21%
Memory 2.55 MB / Beats 37.63%
*/

func subsets(nums []int) [][]int {
    res := make([][]int, 0) 
    res = append(res, []int{})
    
    for _, num := range nums {
        tmp_res := [][]int{}
        for _, res_num := range res {
            tmp_num := append([]int{}, res_num...)
            tmp_num = append(tmp_num, num)
            tmp_res = append(tmp_res, tmp_num)
        }
        res = append(res, tmp_res...)
    } 

    return res
}