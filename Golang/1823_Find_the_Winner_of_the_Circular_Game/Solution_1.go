/*
Runtime 9 ms / Beats 28.57%
Memory 10.84 MB / Beats 11.90%
*/


func findTheWinner(n int, k int) int {
    queue := make([]int, 0, n)
    for i := 1; i <= n; i++ {
        queue = append(queue, i)
    }

    count := 0
    for len(queue) > 1 {
        pop_val := queue[0]
        queue = queue[1:]

        count += 1
        if count == k {
            count = 0
            continue
        }
        queue = append(queue, pop_val)
    }

    return queue[0]
}