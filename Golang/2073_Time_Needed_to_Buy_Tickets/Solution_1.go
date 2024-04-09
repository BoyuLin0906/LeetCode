/*
Runtime 0 ms / Beats 100.00%
Memory 5.38 MB / Beats 5.13%
*/

func timeRequiredToBuy(tickets []int, k int) int {
    t_len := len(tickets)
    queue := make([]int, t_len)
    times := 0
    
    for i := 0; i < t_len; i++ {
        queue[i] = i
    }

    for {
        if tickets[queue[0]] > 0 {
            tickets[queue[0]]--
            times++
        }
        if tickets[k] == 0 && queue[0] == k {
            break
        }
        queue = append(queue[1:t_len], queue[0])
    }

    return times
}