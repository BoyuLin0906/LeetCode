/*
Runtime 37 ms / Beats 52.18%
Memory 6.58 MB / Beats 93.44%
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

    i := min_num
    for i <= max_num {
        if tables[i] > 0 {
            for j := 1; j < groupSize; j++ {
                if tables[i+j] <= 0 || tables[i+j-1] <= 0 {
                    return false
                }
            }
            for j := 0; j < groupSize; j++ {
                tables[i+j] -= 1
            }
        } else {
            i += 1
        }
    } 
    return true
}