/*
Runtime 26 ms / Beats 94.51%
Memory 6.87 MB / Beats 94.51%
*/

func openLock(deadends []string, target string) int {
    int_target, _ := strconv.Atoi(target)
    if int_target == 0 {
        return 0
    } 

    visited_table := make(map[int]bool, 10000)
    for _, deadend := range(deadends) {
        n, _ := strconv.Atoi(deadend)
        visited_table[n] = true
    }

    if visited_table[0] {
        return -1
    }

    queue := []int{0}
    res := 0

    for len(queue) > 0 {
        res++
        queue_len := len(queue)
        for i := 0; i < queue_len; i++ {
            pop_num := queue[0]
            queue = queue[1:len(queue)]
            for _, num := range getAllNums(pop_num) {
                if num == int_target {
					return res
				}
                if !visited_table[num] {
                    queue = append(queue, num)
                    visited_table[num] = true 
                }
            }
        } 
    }
    return -1
}

func getAllNums(num int) []int {
	result := make([]int, 0, 8)
	for place := 1; place <= 1000; place *= 10 {
        for j := -1; j <= 1; j ++ {
            if j == 0 {
                continue
            }
            org_d := (num / place) % 10
            rep_d := (org_d + 10 + j) % 10
            result = append(result, num - org_d * place + rep_d * place)
        }
	}
	return result
}