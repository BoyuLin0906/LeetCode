/*
Runtime 32 ms / Beats 100.00%
Memory 7.75 MB / Beats 28.00%
*/

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
    max_ability := slices.Max(worker)
    jobs := make([]int, max_ability+1)
    
    for idx, lvl := range difficulty {
        if lvl <= max_ability {
            jobs[lvl] = max(jobs[lvl],  profit[idx])
        }
    }

    for i := 1; i < max_ability+1; i++ {
        jobs[i] = max(jobs[i], jobs[i-1])
    }

    total_profits := 0
    for _, ability := range worker {
        total_profits += jobs[ability]
    }

    return total_profits
}