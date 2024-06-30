/*
Runtime 282 ms / Beats 19.23%
Memory 31.82 MB / Beats 15.38%
*/

func getAncestors(n int, edges [][]int) [][]int {
    node_graph := make([][]int, n)
    in_degree := make([]int, n)

    for _, edge := range edges{
        node_graph[edge[0]] = append(node_graph[edge[0]], edge[1])
        in_degree[edge[1]] += 1
    }

    visited := make(map[int]map[int]bool, n)
    queue := make([]int, 0, n)
    for i := 0; i < n; i++ {
        if in_degree[i] == 0 {
            queue = append(queue, i)
        }
        visited[i] = make(map[int]bool)
    }
  
    for len(queue) > 0 {
        s_node := queue[0]
        queue = queue[1:]
        for _, nxt_node := range node_graph[s_node] {
            in_degree[nxt_node] -= 1
            visited[nxt_node][s_node] = true
            for node_to_s, _ := range visited[s_node] {
                visited[nxt_node][node_to_s] = true
            }
            if in_degree[nxt_node] == 0 {
                queue = append(queue, nxt_node)
            }
        }
    }
  
    res := make([][]int, n)
    for i := 0; i < n; i++ {
        res[i] = make([]int, 0, len(visited[i]))
        for node, _ := range visited[i] {
            res[i] = append(res[i], node)
        }
        sort.Ints(res[i])
    } 

    return res
}

