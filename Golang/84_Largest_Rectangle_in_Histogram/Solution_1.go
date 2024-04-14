func largestRectangleArea(heights []int) int {
    heights = append([]int{0}, heights...)
    heights = append(heights, 0)
    res := 0

    stack := make([]int, 0)
    for i := 0; i < len(heights); i++ {
        for len(stack) > 0 && heights[stack[len(stack)-1]] > heights[i] {
            pop_index := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            prev_index := stack[len(stack)-1]
            res = max(res, (i - prev_index - 1) * heights[pop_index])
        }
        stack = append(stack, i)
    }

    return res
}