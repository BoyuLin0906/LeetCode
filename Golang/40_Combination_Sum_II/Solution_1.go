/*
Runtime 0 ms / Beats 100.00%
Memory 3.02 MB / Beats 27.36%
*/

func combinationSum2(candidates []int, target int) [][]int {
    counter := make([]int, 51)
    max_c := 0
    min_c := 51
    res := make([][]int, 0)

    for i := 0; i < len(candidates); i++ {
        counter[candidates[i]] += 1
        if candidates[i] > max_c {
            max_c = candidates[i]
        }
        if candidates[i] < min_c {
            min_c = candidates[i]
        }
    }

    for i := max_c; i >= min_c; i-- {
        if counter[i] > 0 {
            combination := []int{}
            sum := 0
            helper(counter, target, min_c, i, combination, sum, &res)
        }
    }

    return res
}

func helper(counter []int, target int, left int, right int, combination []int, sum int, res *[][]int) {
    count := counter[right]

    for count > 0 && sum < target {
        sum += right 
        combination = append(combination, right)
        count--

        if sum < target {
            for r := right-1; r >= left; r-- {
                if counter[r] > 0 {
                    helper(counter, target, left, r, combination, sum, res)
                }
            }
        }

    }

    if sum == target {
        tmp := make([]int, len(combination))
        copy(tmp, combination)
        *res = append(*res, tmp)
    } 
        
    for count != counter[right] {
        count++
        combination = combination[:len(combination)-1]
    }
}