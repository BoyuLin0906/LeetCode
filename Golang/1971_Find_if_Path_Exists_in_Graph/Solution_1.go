/*
Runtime 206 ms / Beats 95.51%
Memory 32.12 MB / Beats 88.02%
*/

func validPath(n int, edges [][]int, source int, destination int) bool {
    tables := make([][]int, n)
    visited := make([]bool, n)
    queue := make([]int, 0)

    for _, edge := range(edges) {
        tables[edge[0]] = append(tables[edge[0]], edge[1])
        tables[edge[1]] = append(tables[edge[1]], edge[0])
    }

    queue = append(queue, source)
    visited[source] = true

    for len(queue) > 0 {
        vertex := queue[0]
        queue = queue[1:len(queue)]
        if vertex == destination {
            return true
        }
        
        for _, next_vertex := range(tables[vertex]) {
            if visited[next_vertex] == false {
                visited[next_vertex] = true
                queue = append(queue, next_vertex)
            }
        }
    }


    return false
}