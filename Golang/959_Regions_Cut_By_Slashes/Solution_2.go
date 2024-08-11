/*
Runtime 3 ms / Beats 77.78%
Memory 2.83 MB / Beats 88.89%
*/

// Union-Find
func regionsBySlashes(grid []string) int {
    gird_len := len(grid)
    parents_arr := make([]int, (gird_len + 1) * (gird_len + 1))

    for i := 0; i < (gird_len + 1); i++ {
        for j := 0; j < (gird_len + 1); j++ {
            if i == 0 || j == 0 || i == gird_len || j == gird_len {
                continue
            }
            parents_arr[i *  (gird_len + 1) + j]  = i *  (gird_len + 1) + j
        }
    }

    uf := &UnionFind{parent: parents_arr}

    res_count := 1
    for i := 0; i < gird_len; i++ {
        for j := 0; j < gird_len; j++ {
            if grid[i][j] == ' ' {
                continue
            }
            point_a := -1
            point_b := -1
            if grid[i][j] == '/' {
                point_a = i * (gird_len + 1) + (j + 1)
                point_b = (i + 1) * (gird_len + 1) + j
            } else {
                point_a = i * (gird_len + 1) + (j)
                point_b = (i + 1) * (gird_len + 1) + (j + 1)
            }

            if uf.Find(point_a) == uf.Find(point_b) {
                res_count++
            } else {
                uf.Union(point_a, point_b)
            }
        }
    }
    
    return res_count
}

type UnionFind struct {
    parent []int
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