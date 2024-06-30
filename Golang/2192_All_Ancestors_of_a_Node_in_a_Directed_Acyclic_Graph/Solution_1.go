/*
Runtime 218 ms / Beats 65.38%
Memory 62.56 MB / Beats 7.69%
*/

func getAncestors(n int, edges [][]int) [][]int {
    node_maps := make(map[int][]int, n)
    res := make([][]int, n)

    for i := 0; i < n; i++ {
        node_maps[i] = make([]int, 0, n)
        res[i] = make([]int, 0, n)
    } 

    for _, edge := range edges{
        node_maps[edge[1]] = append(node_maps[edge[1]], edge[0])
    }

    for i := 0; i < n; i++ {
        visited := make([]bool, n)
        ancestors := make([]int, 0, n)
        dfs(i, node_maps, visited)
        for j := 0; j < n; j++ { 
            if j == i {
                continue
            }
            if visited[j] {
                ancestors = append(ancestors, j)
            }
        }
        res[i] = ancestors
    }

    return res
}

func dfs(node int, node_maps map[int][]int, visited []bool) {
    visited[node] = true

    for _, nxt_node := range node_maps[node] {
        if !visited[nxt_node] {
            dfs(nxt_node, node_maps, visited)
        }
    }
}