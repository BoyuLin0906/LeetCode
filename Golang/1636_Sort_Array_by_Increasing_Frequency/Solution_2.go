/*
Runtime 0 ms / Beats 100.00%
Memory 2.92 MB / Beats 95.35%
*/

func frequencySort(nums []int) []int {
    num_freq := make([]int, 201)
    for _, num := range nums {
        num_freq[num+100] += 1
    }

    sort.Slice(nums, func(i, j int) bool {
        if num_freq[nums[i]+100] == num_freq[nums[j]+100] {
            return nums[i] > nums[j]
        }
		return num_freq[nums[i]+100] < num_freq[nums[j]+100]
	})

    return nums
}