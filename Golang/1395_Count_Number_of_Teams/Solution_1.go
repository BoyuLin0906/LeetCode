/*
Runtime 9 ms / Beats 91.30%
Memory 2.84 MB / Beats 82.61%
*/
func numTeams(rating []int) int {
    sum := 0
    rating_len := len(rating)

    for j := 0; j < rating_len; j++ {
        left := 0
        right := 0

        for i := 0; i < j ; i++ {
            if rating[i] < rating[j] {
                left++
            }
        }

        for k := j+1; k < rating_len; k++ {
            if rating[j] < rating[k] {
                right++
            }
        }

        sum += (left * right) + ((j-left) * (rating_len-1-j-right))
    }

    return sum
}

