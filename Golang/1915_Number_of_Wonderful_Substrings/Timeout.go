func wonderfulSubstrings(word string) int64 {

    prefix_sum := make(map[int]uint, len(word))
    var res int64 = 0
    prefix_sum[0] = 1 << (word[0] - 'a')
    res++
    for i := 1; i < len(word); i ++ {
        prefix_sum[i] = prefix_sum[i-1] ^ 1 << (word[i] - 'a') 
        if bits.OnesCount(prefix_sum[i]) <= 1 {
            res++
        }
        for j := 0; j < i; j++ {
            if bits.OnesCount(prefix_sum[i] ^ prefix_sum[j])<= 1 {
                res++
            }
        }
    }

    return res
}