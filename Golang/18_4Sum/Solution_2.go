/*
Runtime 10 ms / Beats 69.72%
Memory 2.89 MB / Beats 84.86%
*/

func fourSum(nums []int, target int) [][]int {

    sort.Ints(nums)

    nums_len := len(nums)
    result := make([][]int, 0)
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
                    res := []int{nums[i], nums[j], nums[left_idx], nums[right_idx]}
                    result = append(result, res)
                    for left_idx < right_idx && nums[left_idx] == nums[left_idx+1] {
                        left_idx++
                    }
                    for left_idx < right_idx && nums[right_idx] == nums[right_idx-1] {
                        right_idx--
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