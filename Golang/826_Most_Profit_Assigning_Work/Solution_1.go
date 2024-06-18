/*
Runtime 63 ms / Beats 44.00%
Memory 7.02 MB / Beats 92.00%
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
    fmt.Println(jobs)

    for i := 0; i < len(difficulty)-1; i++{
        jobs[i+1].profit = max(jobs[i+1].profit, jobs[i].profit)
    }

    total_profits := 0
    for _, ability := range worker {
        max_profit := 0

        left_idx, right_idx := 0, len(jobs)-1
        for left_idx <= right_idx {
            mid_idx := (left_idx + right_idx) / 2
            if jobs[mid_idx].difficulty <= ability {
                max_profit = max(max_profit, jobs[mid_idx].profit)
                left_idx = mid_idx + 1
            } else {
                right_idx = mid_idx - 1
            }
        }
        total_profits += max_profit
    }

    return total_profits
}