/*
Runtime 3 ms / Beats 68.18%
Memory 3.08 MB / Beats 66.67%
*/

func minOperations(logs []string) int {
    count := 0
    for _, log := range logs {
        if log == "../" {
            if count > 0 {
                count -= 1
            }
        } else if log == "./" {
            continue
        } else {
            count += 1
        }
    }
    return count
}