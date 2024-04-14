/*
Runtime 8 ms / Beats 70.17%
Memory 6.16 MB / Beats 24.86%
*/


func trap(height []int) int {
    stack := make([]int, 0)
    index := 0
    res := 0

    for index < len(height) {
        if len(stack) == 0 || height[stack[len(stack)-1]] > height[index] {
            stack = append(stack, index)
            index++
        } else {
            min_index := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            if len(stack) == 0 {
                continue
            }

            prev_index := stack[len(stack)-1]
            trapped_height := min(height[prev_index], height[index]) - height[min_index]
            trapped_width := index - prev_index - 1
            res += (trapped_height * trapped_width)
        }
    }

    return res
}