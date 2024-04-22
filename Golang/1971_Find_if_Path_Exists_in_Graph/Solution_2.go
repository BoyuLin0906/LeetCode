type UnionFind struct {
    parent []int
}

func NewUnionFind(n int) *UnionFind {
    parent := make([]int, n)
    for i := 0; i < n; i ++ {
        parent[i] = i
    }
    return &UnionFind{parent: parent}
}

func (uf *UnionFind) Find(num int) int {
    if uf.parent[num] == num {
        return num
    }
    return uf.Find(uf.parent[num])
}

func (uf *UnionFind) Union(num1, num2 int) {
    i := uf.Find(num1)
    j := uf.Find(num2)

    if i > j {
        uf.parent[i] = j
    } else {
        uf.parent[j] = i
    }
}



func validPath(n int, edges [][]int, source int, destination int) bool {
    union_find_obj := NewUnionFind(n)

    for _, edge := range(edges) {
        union_find_obj.Union(edge[0], edge[1])
    }

    return union_find_obj.Find(source) == union_find_obj.Find(destination)
}