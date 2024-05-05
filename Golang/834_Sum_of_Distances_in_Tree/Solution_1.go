/*
Runtime 224 ms / Beats 9.89%
Memory 18.51 MB / Beats 27.12%
*/

func sumOfDistancesInTree(n int, edges [][]int) []int {
    edge_graph := make(map[int][]int)

    for _, edge := range edges {
        edge_graph[edge[0]] = append(edge_graph[edge[0]], edge[1])
        edge_graph[edge[1]] = append(edge_graph[edge[1]], edge[0])
    }

    // all count
    count := make([]int, n)
    dfs_count(-1, 0, count, edge_graph)

    // root total
    total := make([]int, n)
    total[0] = dfs_root_total(-1, 0, count, edge_graph)

    // all total
    dfs_all_total(-1, 0, count, total, edge_graph)
    return total
}

func dfs_count(parent int, current int, count []int, edge_graph map[int][]int) int {
    sum := 1
    for _, node := range edge_graph[current] {
        if parent == node {
            continue
        }
        sum += dfs_count(current, node, count, edge_graph)
    }
    count[current] = sum
    return sum
}

func dfs_root_total(parent int, current int, count []int, edge_graph map[int][]int) int {
    sum := 0
    for _, node := range edge_graph[current] {
        if parent == node {
            continue
        }
        sum += dfs_root_total(current, node, count, edge_graph)
    }
    sum += count[current] - 1
    return sum
}

func dfs_all_total(parent int, current int, count []int, total []int, edge_graph map[int][]int) {
    for _, node := range edge_graph[current] {
        if parent == node {
            continue
        }
        b := count[node] 
        a := len(total) - b
        total[node] = total[current] + a - b
        dfs_all_total(current, node, count, total, edge_graph)
    }
}