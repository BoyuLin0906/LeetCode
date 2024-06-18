/*
Runtime 464 ms / Beats 12.00%
Memory 6.98 MB / Beats 92.00%
*/

type job struct {
    difficulty int
    profit int
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
    jobs := make([]*job, len(difficulty))
    for idx, lvl := range difficulty {
        jobs[idx] = &job{difficulty: lvl, profit: profit[idx]}
    }

    sort.Slice(jobs, func(i, j int) bool {
		return jobs[i].difficulty < jobs[j].difficulty
	})
    sort.Ints(worker)
    
    total_profits := 0
    for _, ability := range worker {
        max_profit := 0
        idx := 0
        for idx < len(jobs) && jobs[idx].difficulty <= ability {
            max_profit = max(max_profit, jobs[idx].profit)
            idx += 1
        }
        total_profits += max_profit
    }

    return total_profits
}