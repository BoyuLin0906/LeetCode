/*
Runtime 163 ms / Beats 100.00%
Memory 7.30 MB / Beats 100.00%
*/

type JumbledNumber struct {
    Num int
    Index int
    MappedNum int
}

func sortJumbled(mapping []int, nums []int) []int {
    jumbled_nums := make([]*JumbledNumber, len(nums))
    for i := 0; i < len(nums); i++ {
        num := nums[i]
        mapped_num := 0
        if num == 0 {
            mapped_num = mapping[0]
        } else {
            tmp := 1
            for num != 0 {
                mapped_num += mapping[num % 10] * tmp
                tmp *= 10
                num /= 10
            }
        }
        jumbled_nums[i] = &JumbledNumber{Num: nums[i], Index: i, MappedNum: mapped_num}
    }

    sort.Slice(jumbled_nums, func(i, j int) bool {
        if jumbled_nums[i].MappedNum == jumbled_nums[j].MappedNum {
            return jumbled_nums[i].Index < jumbled_nums[j].Index
        }
		return jumbled_nums[i].MappedNum < jumbled_nums[j].MappedNum
	})

    for i := 0; i < len(nums); i++ {
        nums[i] = jumbled_nums[i].Num
    }

    return nums
}