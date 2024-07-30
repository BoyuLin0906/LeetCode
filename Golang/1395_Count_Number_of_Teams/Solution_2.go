/*
Runtime 4 ms / Beats 100.00%
Memory 7.56 MB / Beats 7.69%
*/

/* 
   1. using BIT to get rating frequency
   2. LEFT BIT & RIGHT BIT to count smaller rating
*/
func numTeams(rating []int) int {
    max_rating := slices.Max(rating)

    left_BIT := make([]int, max_rating+1)
    right_BIT := make([]int, max_rating+1)

    for _, r := range rating {
        update_BIT(right_BIT, r, 1)
    }

    sum := 0
    for index, r := range rating {
        update_BIT(right_BIT, r, -1)

        left_smaller := get_prefix_sum(left_BIT, r-1)
        right_smaller := get_prefix_sum(right_BIT, r-1)
        left_bigger := index-left_smaller
        right_bigger := len(rating)-1-index-right_smaller
        
        sum += left_smaller * right_bigger + left_bigger * right_smaller

        update_BIT(left_BIT, r, 1)
    }
    return sum
}

func update_BIT(BIT []int, index int, value int) {
    for index < len(BIT) {
        BIT[index] += value
        index += index & (-index)
    }
}

func get_prefix_sum(BIT []int, index int) int {
    sum := 0
    for index > 0 {
        sum += BIT[index]
        index -= index & (-index)
    }
    return sum
}