/*
Runtime 85 ms / Beats 63.74%
Memory 7.17 MB / Beats 78.02%
*/

func openLock(deadends []string, target string) int {
    if target == "0000" {
        return 0
    } 

    visited_table := make(map[string]bool)
    for _, deadend := range(deadends) {
        visited_table[deadend] = true
    }

    if visited_table["0000"] {
        return -1
    }

    queue := make([][]byte, 0)
    queue = append(queue, []byte{'0', '0', '0', '0'})
    res := 0

    for len(queue) > 0 {
        res++
        queue_len := len(queue)
        for i := 0; i < queue_len; i++ {
            pop_value := queue[0]
            queue = queue[1:len(queue)]
            for i := 0; i < 4; i++ {
                for j := -1; j <= 1; j ++ {
                    if j == 0 {
                        continue
                    }
                    copy_value := make([]byte, 4)
                    copy(copy_value, pop_value)
                    copy_value[i] = byte(((int(copy_value[i]) - 48 + j + 10) % 10) + 48)
                    copy_str := string(copy_value)
                    if copy_str == target {
                        return res
                    }
                    if !visited_table[copy_str] {
                        queue = append(queue, copy_value)
                    }
                    visited_table[copy_str] = true
                } 
            }

        } 
    }
    return -1
}