/*
Runtime 32 ms / Beats 71.98%
Memory 8.04 MB / Beats 14.41%
*/

func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand) % groupSize != 0 {
        return false
    }

    tables := make(map[int]int)
    sort.Ints(hand)
    for _, val := range hand {
        tables[val] += 1
    }

    for _, val := range hand {
        if tables[val] == 0 {
            continue
        }

        for j := 0; j < groupSize; j++ {
            if tables[val+j] == 0 {
                return false
            }
            tables[val+j]--
        }
    }

    return true
}