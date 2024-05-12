/*
Runtime 7 ms / Beats 94.00%
Memory 5.48 MB / Beats 82.00%
*/

type rank struct {
	index int
	score int
}

func findRelativeRanks(score []int) []string {
    rank_slice := make([]*rank, len(score))
	for idx, sc := range score {
		rank_slice[idx] = &rank{idx, sc}
	}

	sort.Slice(rank_slice, func(i, j int) bool {
		return rank_slice[i].score > rank_slice[j].score
	})

	res := make([]string, len(score))
	for idx, rank := range rank_slice {
		if idx > 2 {
			res[rank.index] = strconv.Itoa(idx + 1)
			continue
		}

		if idx == 0 {
			res[rank.index] = "Gold Medal"
		} else if idx == 1 {
			res[rank.index] = "Silver Medal"
		} else if idx == 2 {
			res[rank.index] = "Bronze Medal"
		}
	}

	return res
}