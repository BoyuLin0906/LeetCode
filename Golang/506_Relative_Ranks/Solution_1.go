func findRelativeRanks(score []int) []string {
    sort_score := make([]int, len(score))
    copy(sort_score, score)
    sort.Ints(sort_score)

    res := make([]string, len(score))
    count := 1
    for len(sort_score) > 0 { 
        last_score := sort_score[len(sort_score)-1]
        for idx, sc := range score {
            if sc == last_score {
                if count == 1 {
                    res[idx] = "Gold Medal"
                } else if count == 2 {
                    res[idx] = "Silver Medal"
                } else if count == 3 {
                    res[idx] = "Bronze Medal"
                } else {
                    res[idx] = strconv.Itoa(count)
                }
            }
        }
        count++
        sort_score = sort_score[:len(sort_score)-1]
    }
    return res
}