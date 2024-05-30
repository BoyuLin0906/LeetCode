/*
Runtime 1 ms / Beats 82.35%
Memory 2.37 MB / Beats 58.82%
*/

func countTriplets(arr []int) int {
    prefix_sum := make([]int, len(arr)+1)
    prefix_sum[0] = 0
    for i := 1; i < len(arr)+1; i++ {
        prefix_sum[i] = prefix_sum[i-1] ^ arr[i-1]
    }
    /* 
        arr : [2 3 1 6 7]
        prefix_sum : [0 2 1 0 6 1]

        [ {A B} {C D E} F G] -> {A B} == {C D E} -> {A B} ^ {C D E} = 0 -> A ^ B ^ C ^ D ^ E = 0
        > {A} {B C D E}, {A B} {C D E}, {A B C} {D E}, {A B C D} {E} -> 4
    */
    res := 0
    for i := 0; i < len(arr)+1; i++ {
        for j := i+1; j < len(arr)+1; j++ {
            if prefix_sum[i] == prefix_sum[j] {
                res += j - i - 1
            }
        }
    }

    return res
}