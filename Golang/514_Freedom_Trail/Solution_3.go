/*
Runtime 59 ms / Beats 16.67%
Memory 6.76 MB / Beats 83.33%
*/

func findRotateSteps(ring string, key string) int {
    ring_len := len(ring)
    key_len := len(key)
    
    best_steps := make([][]int, ring_len)
    for i := 0; i < ring_len; i++ {
        best_steps[i] = make([]int, key_len+1)
        for j := 0; j < key_len+1; j++ {
            best_steps[i][j] = math.MaxInt64
        }
    }

    for i := 0; i < ring_len; i++ {
        best_steps[i][key_len] = 0
    } 


    for key_idx := key_len-1; key_idx > -1; key_idx-- {
        for ring_idx := 0; ring_idx < ring_len;  ring_idx++ {
            for char_idx := 0; char_idx < ring_len; char_idx++ {
                if ring[char_idx] == key[key_idx] {
                    
                    diff := char_idx - ring_idx
                    if diff < 0 {
                        diff = -diff
                    }
                    sum := min(diff, ring_len - diff)
                    best_steps[ring_idx][key_idx] = min(best_steps[ring_idx][key_idx],
                                                        1 + sum + best_steps[char_idx][key_idx+1])
                }
            }
        }
    }
    
    return best_steps[0][0]
}