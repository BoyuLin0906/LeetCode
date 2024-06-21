/*
Runtime 25 ms / Beats 87.50%
Memory 6.73 MB / Beats 31.25%
*/

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
    not_grumpy_satisfied := 0
    for i := 0; i < minutes; i++ {
        if grumpy[i] == 1 {
            not_grumpy_satisfied += customers[i]
        }
    }

    total_satisfied := 0
    max_not_grumpy_satisfied := not_grumpy_satisfied
    for i := 0; i < len(customers); i++ {
        if grumpy[i] == 0 {
            total_satisfied += customers[i]
        }
        if i + minutes < len(customers) {
            if grumpy[i] == 1 {
                not_grumpy_satisfied -= customers[i]
            }
            if grumpy[i + minutes] == 1 {
                not_grumpy_satisfied += customers[i + minutes]
            }
            max_not_grumpy_satisfied = max(max_not_grumpy_satisfied, not_grumpy_satisfied)
        }
    }

    return total_satisfied + max_not_grumpy_satisfied
}