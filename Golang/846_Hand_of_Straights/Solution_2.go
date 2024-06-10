/*
Runtime 31 ms / Beats 76.46%
Memory 6.97 MB / Beats 69.83%
*/

func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand) % groupSize != 0 {
        return false
    }

    tables := make(map[int]int)
    max_num := math.MinInt
    min_num := math.MaxInt
    for _, val := range hand {
        tables[val] += 1
        if val < min_num {
            min_num = val
        }
        if val > max_num {
            max_num = val
        }
    }

    for i := min_num; i <= max_num; i++ {
        if tables[i] == 0 {
            continue
        }

        for tables[i] > 0 {
            for j := 0; j < groupSize; j++ {
                if tables[i+j] == 0 {
                    return false
                }
                tables[i+j]--
            }
        }
    }
    return true
}