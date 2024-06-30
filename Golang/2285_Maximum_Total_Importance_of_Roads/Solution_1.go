/*
Runtime 207 ms / Beats 36.97%
Memory 11.27 MB / Beats 64.52%
*/

func maximumImportance(n int, roads [][]int) int64 {
    node_count := make([]int, n)
    node_keys := make([]int, n)
    importants := make([]int, n)

    for i := 0; i < n; i++{
        node_keys[i] = i
    }

    for _, road := range roads {
        node_count[road[0]] += 1
        node_count[road[1]] += 1
    }

    sort.SliceStable(node_keys, func(i, j int) bool{
        return node_count[node_keys[i]] < node_count[node_keys[j]]
    })
    
    for i := 0; i < n; i++{
        importants[node_keys[i]] = i+1
    }

    sum := 0
    for _, road := range roads {
       sum += importants[road[0]] + importants[road[1]]
    }

    return int64(sum)
}