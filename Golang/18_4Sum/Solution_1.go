/*
Runtime 7 ms / Beats 83.26%
Memory 3.02 MB / Beats 33.03%
*/

func fourSum(nums []int, target int) [][]int {

    sort.Ints(nums)

    nums_len := len(nums)
    result := make([][]int, 0)
    check := make(map[string]bool)
    for i := 0; i < nums_len; i++ {
        if i > 0 && nums[i-1] == nums[i] {
            continue
        }

        for j := i+1; j < nums_len; j++ { 
            if j > i+1 && nums[j-1] == nums[j] {
                continue
            }

            left_idx := j+1
            right_idx := nums_len-1

            for left_idx < right_idx {
                sum := nums[i] + nums[j] + nums[left_idx] + nums[right_idx]
                if sum == target {
                    key := fmt.Sprintf("%d,%d,%d,%d", nums[i], nums[j], nums[left_idx], nums[right_idx])
                    if !check[key] {
                        res := []int{nums[i], nums[j], nums[left_idx], nums[right_idx]}
                        result = append(result, res)
                        check[key] = true
                    }
                    right_idx--
                    left_idx++
                } else if sum > target {
                    right_idx--
                } else {
                    left_idx++
                }
            }
        }
    }

    return result
}