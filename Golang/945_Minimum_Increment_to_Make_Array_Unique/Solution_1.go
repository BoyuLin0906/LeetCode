/*
Runtime 101 ms / Beats 100.00%
Memory 12.16 MB / Beats 11.11%
*/

func minIncrementForUnique(nums []int) int {
    counter := make([]int, 200000)
    moves := 0

    for _, num := range nums {
        if counter[num] == 0 {
            counter[num] = 1
        } else {
            moves += counter[num]
            counter[num+1] += counter[num]
            counter[num] = 1
        }
    }

    for i := 0; i < 200000; i++ {
        if counter[i] > 1 {
            moves += counter[i] - 1
            counter[i+1] += counter[i] - 1
        }
    }

    return moves
}