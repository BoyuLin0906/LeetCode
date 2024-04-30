/*
Runtime 18 ms / Beats 100.00%
Memory 6.18 MB / Beats 100.00%
*/

func wonderfulSubstrings(word string) int64 {
    
    counter := make([]int64, 1024)
    var res int64 = 0
    counter[0] = 1
    xor_sum := 0

    for i := 0; i < len(word); i ++ {
        xor_sum ^= (1 << (word[i] - 'a'))
        res += counter[xor_sum] // even solution -> even XOR even -> OK

        for j := 0; j < 10; j++ {
            res += counter[xor_sum ^ (1 << j)] // one odd solution -> OK
        }
        counter[xor_sum]++
    }

    return res
}