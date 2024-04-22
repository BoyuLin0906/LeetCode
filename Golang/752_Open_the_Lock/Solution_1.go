/*
Runtime 813 ms / Beats 5.49%
Memory 8.19 MB / Beats 15.38%
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

    queue := make([][]int, 0)
    queue = append(queue, []int{0, 0, 0, 0})
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
                    copy_value := make([]int, 4)
                    copy(copy_value, pop_value)
                    copy_value[i] = (copy_value[i] + j + 10) % 10
                    copy_str := strings.Trim(strings.Join(strings.Split(fmt.Sprint(copy_value), " "), ""), "[]")
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