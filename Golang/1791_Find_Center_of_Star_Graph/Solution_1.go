/*
Runtime 122 ms / Beats 33.04%
Memory 15.02 MB / Beats 88.39%
*/


func findCenter(edges [][]int) int {
    counter := make(map[int]int, 0)

    for _, edge := range edges {
        counter[edge[0]] += 1
        counter[edge[1]] += 1
    }

    max_count := 0
    center := -1
    for node, count := range counter {
        if count > max_count {
            max_count = count
            center = node
        }
    }

    return center
}