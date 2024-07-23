/*
Runtime 0 ms / Beats 100.00%
Memory 3.59 MB / Beats 18.60%
*/

type NumFreq struct {
    num int
    freq int
}

func frequencySort(nums []int) []int {
    
    num_freq := make(map[int]int, len(nums))
    for _, num := range nums {
        num_freq[num] += 1
    }

    num_freq_struct := make([]*NumFreq, 0, len(num_freq))
    for num, freq := range num_freq {
        num_freq_struct = append(num_freq_struct, &NumFreq{num: num, freq: freq})
    }

    sort.Slice(num_freq_struct, func(i, j int) bool {
        if num_freq_struct[i].freq == num_freq_struct[j].freq {
            return num_freq_struct[i].num > num_freq_struct[j].num
        }
		return num_freq_struct[i].freq < num_freq_struct[j].freq
	})

    res := make([]int, 0, len(nums))
    for _, num_freq := range num_freq_struct {
        for i := 0; i < num_freq.freq; i++ {
            res = append(res, num_freq.num)
        }
    }

    return res
}