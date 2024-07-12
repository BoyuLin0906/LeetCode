/*
Runtime 26 ms / Beats 88.89%
Memory 6.97 MB / Beats 88.89%
*/

func maximumGain(s string, x int, y int) int {
    substring := []rune{'a', 'b'}
    if x < y {
        substring = []rune{'b', 'a'}
        x, y = y, x
    }
    
    head_count := 0
    tail_count := 0
    res := 0

    for _, char := range s {
        if char == substring[0] {
            head_count += 1
        } else if char == substring[1] {
            if head_count > 0 {
                head_count -= 1
                res += x
            } else {
                tail_count += 1
            }
        } else {
            res += min(head_count, tail_count) * y
            head_count = 0
            tail_count = 0
        }
    }

    res += min(head_count, tail_count) * y
    return res
}