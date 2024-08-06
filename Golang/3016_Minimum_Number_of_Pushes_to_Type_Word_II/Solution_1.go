/*
Runtime 18 ms / Beats 100.00%
Memory 6.96 MB / Beats 70.83%
*/

func minimumPushes(word string) int {

    letters := make([]int, 26)
    for _, c := range word {
        letters[c - 'a'] += 1
    }

    sort.Slice(letters, func(i, j int) bool {
		return letters[i] > letters[j]
	})

    multiple := 1
    res := 0

    for idx, val := range letters {
        if val == 0 {
            break
        }

        if idx % 8 == 0 && idx != 0 {
            multiple += 1
        }

        res += multiple * val
    }

    return res
}