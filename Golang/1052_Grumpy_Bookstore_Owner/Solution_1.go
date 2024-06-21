/*
Runtime 170 ms / Beats 6.25%
Memory 6.54 MB / Beats 68.75%
*/

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
    total_satisfied := 0
    for i := 0; i < len(customers); i++ {
        if grumpy[i] == 0 {
            total_satisfied += customers[i]
        }
    }
    
    max_satisfied := total_satisfied
    for i := 0; i < len(customers) - minutes + 1; i++ {
        tmp_satisfied := total_satisfied
        fmt.Println(i)
        for j := i; j < i + minutes; j ++ {
            if grumpy[j] == 1 {
                tmp_satisfied += customers[j]
            }
        }
        max_satisfied = max(max_satisfied, tmp_satisfied)
    }

    return max_satisfied
}