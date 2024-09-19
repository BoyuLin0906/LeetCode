/*
Runtime 0 ms / Beats 100.00%
Memory 3.02 MB / Beats 17.24%
*/

func largestNumber(nums []int) string {
    str_nums := make([]string, len(nums))

    for idx, num := range nums {
        str := strconv.Itoa(num)
        str_nums[idx] = str
    }

    sort.Slice(str_nums, func(a, b int) bool {
        return str_nums[b]+str_nums[a] < str_nums[a]+str_nums[b]
    })
    
    if str_nums[0] == "0" {
        return "0"
    }

    str_res := ""
    for _, str_num := range str_nums {
        str_res += str_num
    }

    return str_res
}