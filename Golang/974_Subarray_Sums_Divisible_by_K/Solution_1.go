/*
Runtime 32 ms / Beats 75.76%
Memory 6.75 MB / Beats 93.94%
*/

func subarraysDivByK(nums []int, k int) int {
    prefix_sum_dict := make(map[int]int)
    count, prefix_sum := 0, 0
    prefix_sum_dict[0] = 1

    /*
    1. (prefixSum[j] - prefixSum[i]) % k = 0 -> prefixSum[j] % k = prefixSum[i] % k
        k = 5, A[2, 3] B[ 5 ] C[1, 4] : 
            > A -> 1, [2, 3]
            > A B -> [2, 3] [ 5 ]
            > B -> [5]
            > A B C [2, 3] [ 5 ] [1, 4]
            > B C [ 5 ] [1, 4]
            > C [1, 4]
        so, to A (same prefix mod k) = 1
            to B (same prefix mod k) = 1+1
            to C (same prefix mod k) = 2+1
    2. negative prefix value need to convert to positve
       > nums[i] % k + k -> postive
    */
    for i := 0; i < len(nums); i++ {
        prefix_sum = (prefix_sum + (nums[i] % k + k)) % k
        count += prefix_sum_dict[prefix_sum]
        prefix_sum_dict[prefix_sum] += 1
    } 

    return count
}