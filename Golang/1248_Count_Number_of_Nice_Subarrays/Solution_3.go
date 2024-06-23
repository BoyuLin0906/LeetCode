/*
Runtime 90 ms / Beats 60.00%
Memory 10.61 MB / Beats 15.38%
*/

func numberOfSubarrays(nums []int, k int) int {

    queue := make([]int,0 , len(nums))
    gap := -1
    last_head := -1
    res := 0

    for i := 0; i < len(nums); i++ {
       if nums[i] % 2 == 1 {
            queue = append(queue, i)
       }

        if len(queue) > k {
                last_head = queue[0]
                queue = queue[1:]
        }
        
        if len(queue) == k {
            gap = queue[0] - last_head
            res += gap
        }
        
    }

    return res 
}