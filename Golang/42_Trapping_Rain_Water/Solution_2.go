func trap(height []int) int {

    left_index := 0
    right_index := len(height) - 1
    res := 0
    temp_min_height := 0

    for left_index < right_index {
        min_height := min(height[left_index], height[right_index])
        if min_height == height[left_index] {
            left_index++
        } else {
            right_index--
        }

        temp_min_height = max(temp_min_height, min_height)
        res += temp_min_height - min_height
    }

   
    return res
}