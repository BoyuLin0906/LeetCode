/*
Runtime 5 ms / Beats 100.00%
Memory 7.60 MB / Beats 16.67%
*/

func findRotateSteps(ring string, key string) int {
    ring_len := len(ring)
    key_len := len(key)
    
    step_tables := make([][]int, ring_len)
    for i := 0; i < ring_len; i++ {
        step_tables[i] = make([]int, key_len)
        for j := 0; j < key_len; j++ {
            step_tables[i][j] = -1
        }
    }

    index_mapping := make(map[byte][]int)
    for i := 0; i < ring_len; i++ {
        index_mapping[ring[i]] = append(index_mapping[ring[i]], i)
    } 
    
    return dfs(0, ring_len, 0, key, index_mapping, step_tables) + key_len
}

func dfs(ring_idx int, ring_len int, key_idx int, key string, mapping map[byte][]int, tables [][]int) int {
    if key_idx == len(key) {
        return 0
    }

    if tables[ring_idx][key_idx] != -1 {
        return tables[ring_idx][key_idx]
    }

    sum := math.MaxInt
    for _, idx := range mapping[key[key_idx]] {
        diff := ring_idx - idx
        if diff < 0 {
            diff = -diff
        }
        dfs_sum := dfs(idx, ring_len, key_idx+1, key, mapping, tables)
        sum = min(sum, dfs_sum + min(diff, ring_len - diff))
    }

    tables[ring_idx][key_idx] = sum
    return sum
}
