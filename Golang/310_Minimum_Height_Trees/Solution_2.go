/*
Runtime 56 ms / Beats 84.76%
Memory 7.42 MB / Beats 98.10%
*/


func findMinHeightTrees(n int, edges [][]int) []int {

    if n == 1 {
        return []int{0}
    }

    table := make([][]int, n)
    queue := make([]int, 0)
    degree := make([]int, n)

    for _, edge := range(edges) {
        table[edge[0]] = append(table[edge[0]], edge[1])
        table[edge[1]] = append(table[edge[1]], edge[0])
        degree[edge[0]]++
		degree[edge[1]]++
    }

    for edge, d := range degree {
        if d == 1 {
            queue = append(queue, edge)
        }
    }

    for n > 2 {
        queue_len := len(queue)
        n = n - queue_len
        for i := 0; i < queue_len; i++ {
            edge := queue[i]
            for _, next_edge := range table[edge] {
                degree[next_edge]--
                if degree[next_edge] == 1 {
                    queue = append(queue, next_edge)
                }
            }    
        }
        queue = queue[queue_len:]
    }
    return queue
}