/*
Runtime 3 ms / Beats 68.24%
Memory 4.86 MB / Beats 20.61%
*/

func combinationSum2(candidates []int, target int) [][]int {
    res := make([][]int, 0)
    sort.Ints(candidates)
    helper(candidates, target, []int{}, 0, 0, &res)
    return res
}

func helper(candidates []int, target int, combination []int, sum int, start_idx int, res *[][]int) {
    if sum > target {
        return
    }

    if sum == target {
        *res = append(*res, append([]int{}, combination...))
        return
    } 
    
    for i := start_idx; i < len(candidates); i++ {
        if i != start_idx && candidates[i] == candidates[i - 1] { 
            continue 
        }
        helper(candidates, target, append(combination, candidates[i]), sum + candidates[i], i+1, res)
    }
}