/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/*
Runtime 126 ms / Beats 81.82%
Memory 8.43 MB / Beats 90.91%
*/

func nodesBetweenCriticalPoints(head *ListNode) []int {
    far_prev_val := 0
    prev_val := 0
    cur_idx := 0
    
    max_dis := math.MinInt
    min_dis := math.MaxInt
    first_critical_idx := 0
    prev_critical_idx := 0
    res := []int{-1, -1}

    for head != nil {
        if cur_idx != 0 && cur_idx != 1 {
            cur := head.Val
            if (prev_val > far_prev_val && prev_val > cur) || (prev_val < far_prev_val && prev_val < cur) {
                if first_critical_idx == 0 {
                    first_critical_idx = cur_idx
                } else {
                    min_dis = min(min_dis, cur_idx - prev_critical_idx) 
                }
                prev_critical_idx = cur_idx
            }
            far_prev_val = prev_val
            prev_val = cur
        } else {
            if cur_idx == 0 {
                far_prev_val = head.Val
            } else {
                prev_val = head.Val
            }
        }

        cur_idx += 1
        head = head.Next
    }
    
    if min_dis != math.MaxInt {
        max_dis = prev_critical_idx - first_critical_idx
        res[0], res[1] = min_dis, max_dis
    }
    
    return res
}