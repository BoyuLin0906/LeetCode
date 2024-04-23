/*
Runtime 715 ms / Beats 5.71%
Memory 8.39 MB / Beats 68.57%
*/

type edgeObj struct {
    Edge int
    Visited bool
}

func findMinHeightTrees(n int, edges [][]int) []int {

    if n == 1 {
        return []int{0}
    }

    table := make([][]*edgeObj, n)
    queue := make([]int, 0)

    for _, edge := range(edges) {
        table[edge[0]] = append(table[edge[0]], &edgeObj{Edge: edge[1], Visited: false})
        table[edge[1]] = append(table[edge[1]], &edgeObj{Edge: edge[0], Visited: false})
    }

    for edge, adj_edges := range table {
        if len(adj_edges) == 1 {
            queue = append(queue, edge)
        }
    }

    for n > 2 {
        queue_len := len(queue)
        n = n - queue_len
        for i := 0; i < queue_len; i++ {
            edge := queue[0]
            queue = queue[1:]
            next_edge_objs := table[edge]
            for _, next_edge_obj := range next_edge_objs {
                count := 0
                for _, obj := range table[next_edge_obj.Edge] {
                    if obj.Edge == edge {
                        obj.Visited = true
                    }
                    if !obj.Visited {
                        count++
                    } 
                }

                if count == 1 {
                    queue = append(queue, next_edge_obj.Edge)
                }
            }
        }
    }
    return queue
}