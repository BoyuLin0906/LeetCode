/*
Runtime 3 ms / Beats 85.42%
Memory 3.17 MB / Beats 70.83%
*/

func minMovesToSeat(seats []int, students []int) int {
    sort.Ints(seats)
    sort.Ints(students)

    res := 0
    for i := 0; i < len(seats); i++ {
        diff := seats[i] - students[i]
        if diff < 0 {
            diff = -diff
        }
        res += diff
    }
    return res
}