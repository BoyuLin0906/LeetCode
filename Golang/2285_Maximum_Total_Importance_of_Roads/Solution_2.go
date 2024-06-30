/*
Runtime 151 ms / Beats 97.27%
Memory 10.14 MB / Beats 96.03%
*/

func maximumImportance(n int, roads [][]int) int64 {
    node_count := make([]int, n)

    for _, road := range roads {
        node_count[road[0]] += 1
        node_count[road[1]] += 1
    }

    sort.Ints(node_count)

    vector := 1
    sum := 0
    for _, node := range node_count {
        sum += node * vector
        vector += 1
    }

    return int64(sum)
}