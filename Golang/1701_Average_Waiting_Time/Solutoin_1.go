/*
Runtime 105 ms / Beats 75.00%
Memory 14.55 MB / Beats 91.67%
*/

func averageWaitingTime(customers [][]int) float64 {

    cur_time := 0
    wait_time := 0
    for _, customer := range customers {
        if cur_time < customer[0] {
            cur_time = customer[0] + customer[1]
            wait_time += customer[1]
        } else {
            cur_time += customer[1]
            wait_time += cur_time - customer[0]
        }
    }
    res := float64(wait_time) / float64(len(customers))
    return res
}