/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 133 ms / Beats 63.64%
Memory 8.73 MB / Beats 90.91%
*/

func nodesBetweenCriticalPoints(head *ListNode) []int {
    far_prev_val := 0
    prev_val := 0
    count := 0
    local_pos := make([]int, 0)

    for head != nil {
        if count != 0 && count != 1 {
            cur := head.Val
            if (prev_val > far_prev_val && prev_val > cur) || (prev_val < far_prev_val && prev_val < cur) {
                local_pos = append(local_pos, count)
            }
            far_prev_val = prev_val
            prev_val = cur
        } else {
            if count == 0 {
                far_prev_val = head.Val
            } else {
                prev_val = head.Val
            }
        }

        count += 1
        head = head.Next
    }
    
    if len(local_pos) < 2 {
        return []int{-1, -1}
    }

    max_dis := local_pos[len(local_pos)-1] - local_pos[0]
    min_dis := math.MaxInt
    for i := 1; i < len(local_pos); i++ {
        min_dis = min(min_dis, local_pos[i]-local_pos[i-1])
    }
    
    return []int{min_dis, max_dis}
}