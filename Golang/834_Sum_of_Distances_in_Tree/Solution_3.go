/*
Runtime 181 ms / Beats 23.45%
Memory 17.58 MB / Beats 38.70%
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

func (obj *DistGraghObj)dfs_count(parent int, current int) {
    obj.count[current] = 1
    for _, node := range obj.graph[current] {
        if parent == node {
            continue
        }
        obj.dfs_count(current, node)
        obj.count[current] +=  obj.count[node]
        obj.ret[current] += obj.ret[node] + obj.count[node]
    }
}

func (obj *DistGraghObj)dfs_ret(parent int, current int) {
    for _, node := range obj.graph[current] {
        if parent == node {
            continue
        }
        b := obj.count[node] 
        a := obj.n - b
        obj.ret[node] = obj.ret[current] + a - b
        obj.dfs_ret(current, node)
    }
}

func (obj *DistGraghObj)get_result() []int {
    obj.dfs_count(-1, 0)
    obj.dfs_ret(-1, 0)
    return obj.ret
}