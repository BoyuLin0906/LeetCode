/*
Runtime 1 ms / Beats 84.62%
Memory 2.26 MB / Beats 38.46%
*/

func timeRequiredToBuy(tickets []int, k int) int {
    t_len := len(tickets)
    times := 0
    
    for tickets[k] != 0 {
       for i := 0; i < t_len; i++ {
            if tickets[i] == 0 {
                continue
            } else if tickets[k] == 0 {
                break
            }
            tickets[i]--
            times++
       }
    }
    return times
}