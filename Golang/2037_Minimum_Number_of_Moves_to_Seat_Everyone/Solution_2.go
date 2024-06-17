/*
Runtime 5 ms / Beats 50.00%
Memory 3.38 MB / Beats 70.83%
*/

func minMovesToSeat(seats []int, students []int) int {
    max_pos := max(slices.Max(seats), slices.Max(students))
    difference := make([]int, max_pos)

    for _, pos := range seats {
        difference[pos-1] += 1
    }

    for _, pos := range students {
        difference[pos-1] -= 1
    }

    total_moves := 0
    unmatch := 0
    for _, diff := range difference {
        if unmatch > 0 {
            total_moves += unmatch
        } else {
            total_moves += -unmatch
        }
        unmatch += diff
    }
    return total_moves
}