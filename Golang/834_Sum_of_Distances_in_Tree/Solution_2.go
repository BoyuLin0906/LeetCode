/*
Runtime 173 ms / Beats 29.24%
Memory 16.99 MB / Beats 44.63%
*/

type DistGraghObj struct {
    n int
    graph   map[int][]int
    count   []int
    ret     []int
}


func sumOfDistancesInTree(n int, edges [][]int) []int {

    graph := make(map[int][]int)
    for _, edge := range edges {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
    }

    solution_obj := &DistGraghObj{n: n, 
                                  graph: graph, 
                                  count: make([]int, n),
                                  ret: make([]int, n)}

    return solution_obj.get_result()
}

func (obj *DistGraghObj)dfs_count(parent int, current int) int {
    sum := 1
    for _, node := range obj.graph[current] {
        if parent == node {
            continue
        }
        sum += obj.dfs_count(current, node)
    }
    obj.count[current] = sum
    return sum
}

func (obj *DistGraghObj)dfs_root_ret(parent int, current int) int {
    sum := 0
    for _, node := range obj.graph[current] {
        if parent == node {
            continue
        }
        sum += obj.dfs_root_ret(current, node)
    }
    sum += obj.count[current] - 1
    return sum
}

func (obj *DistGraghObj)dfs_all_ret(parent int, current int) {
    for _, node := range obj.graph[current] {
        if parent == node {
            continue
        }
        b := obj.count[node] 
        a := obj.n - b
        obj.ret[node] = obj.ret[current] + a - b
        obj.dfs_all_ret(current, node)
    }
}

func (obj *DistGraghObj)get_result() []int {
    obj.dfs_count(-1, 0)
    obj.ret[0] = obj.dfs_root_ret(-1, 0)
    obj.dfs_all_ret(-1, 0)
    return obj.ret
}