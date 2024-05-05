/*
Runtime 146 ms / Beats 56.50%
Memory 14.58 MB / Beats 79.80%
*/

func sumOfDistancesInTree(n int, edges [][]int) []int {

    graph := make([][]int, n)
    for _, edge := range edges {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
    }

    count := make([]int, n)
    ret := make([]int, n)
    dfs_count(graph, -1, 0, count, ret)
    dfs_ret(graph, -1, 0, count, ret)
    return ret
}

func dfs_count(graph [][]int, parent, current int, count, ret []int) {
    count[current] = 1
    for _, node := range graph[current] {
        if parent == node {
            continue
        }
        dfs_count(graph, current, node, count, ret)
        count[current] += count[node]
        ret[current] += ret[node] + count[node]
    }
}

func dfs_ret(graph [][]int, parent, current int, count, ret []int) {
    n := len(count)
    for _, node := range graph[current] {
        if parent == node {
            continue
        }
        ret[node] = ret[current] + n - 2 * count[node] 
        dfs_ret(graph, current, node, count, ret)
    }
}