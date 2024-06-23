/*
Runtime 124 ms / Beats 20.00%
Memory 9.25 MB / Beats 
27.69%
*/

func numberOfSubarrays(nums []int, k int) int {

    index_map := make(map[int]int)
    order := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] % 2 == 1 {
            index_map[order] = i
            order += 1
        }
    }

    if len(index_map) < k {
        return 0
    }

    head_idx := 0
    end_idx := k-1
    res := 0
    for end_idx < len(index_map) {
        pre_head_val, is_ok := index_map[head_idx-1]
        head_sum := index_map[head_idx] + 1
        if is_ok {
            head_sum = index_map[head_idx] - pre_head_val
        }

        end_head_val, is_ok := index_map[end_idx+1]
        end_sum := len(nums) - index_map[end_idx]
        if is_ok {
            end_sum = end_head_val - index_map[end_idx]
        }
        res += head_sum * end_sum
        head_idx += 1
        end_idx += 1
    }

    return res
    
}