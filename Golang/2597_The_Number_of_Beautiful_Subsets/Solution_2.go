/*
Runtime 367 ms / Beats 41.18%
Memory 3.01 MB / Beats 94.12%
*/

func beautifulSubsets(nums []int, k int) int {
    
    counter := make(map[int]int)
    for _, num := range nums {
        counter[num] = 0
    }

    return helper(nums, k, 0, &counter)-1
}

func helper(nums []int, diff int, index int, counter *map[int]int) int {
    if len(nums) == index {
            return 1
    }

    skip := helper(nums, diff, index+1, counter)
    take := 0
    if (*counter)[nums[index] - diff] == 0 && (*counter)[nums[index] + diff] == 0 {
        (*counter)[nums[index]]++
        take = helper(nums, diff, index+1, counter)
        (*counter)[nums[index]]--
    }
    return skip + take

}
