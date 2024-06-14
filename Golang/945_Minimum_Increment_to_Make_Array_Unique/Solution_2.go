/*
Runtime 94 ms / Beats 100.00%
Memory 9.87 MB / Beats 22.22%
*/

func minIncrementForUnique(nums []int) int {
    counter := make([]int, 100002)
    moves := 0

    for _, num := range nums {
        counter[num] += 1
    }

    idx := 0
    for len(counter) > idx {
        if counter[idx] > 1 {
            moves += counter[idx] - 1
            if len(counter) <= idx+1 {
                counter = append(counter, counter[idx]-1)
            } else {
                counter[idx+1] += counter[idx]-1
            }
        }
        idx += 1
    }  

    return moves
}