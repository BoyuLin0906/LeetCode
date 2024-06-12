/*
Runtime 1 ms / Beats 77.20%
Memory 2.30 MB / Beats 6.93%
*/

func sortColors(nums []int)  {
    colors := make(map[int]int, 3)
    for _, num := range nums {
        colors[num] += 1
    }

    idx := 0
    for i := 0; i < 3; i++ {
        for colors[i] > 0 {
            nums[idx] = i
            colors[i] -= 1
            idx += 1
        }
    }
}