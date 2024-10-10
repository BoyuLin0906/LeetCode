/*
Runtime 194 ms / Beats 54.54%
Memory 20.15 MB / Beats 48.48%
*/

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
    
    managers := make(map[int][]int, 0)
    for unique_id, manager_id := range manager {
        managers[manager_id] = append(managers[manager_id], unique_id)
    }

    return helper(headID, managers, informTime)
}

func helper(head_id int, manager map[int][]int, informTime []int) int {
    
    max_cost_time := 0
    for _, unique_id := range manager[head_id] {
        cost_time := helper(unique_id, manager, informTime)
        max_cost_time = max(max_cost_time, cost_time)
    }

    return max_cost_time + informTime[head_id]
}