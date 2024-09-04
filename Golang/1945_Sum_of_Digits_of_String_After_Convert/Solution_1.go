/*
Runtime 1 ms / Beats 74.42%
Memory 2.27 MB / Beats 76.74%
*/

func getLucky(s string, k int) int {
    sum := 0

    for _, c := range s {
        val := int(c - 'a' + 1)
        for val != 0 {
            sum += val % 10
            val = val / 10
        }
    }
    
    for i := 0; i < k-1; i ++ {
        tmp_sum := 0
        for sum != 0 {
            tmp_sum += sum % 10
            sum = sum / 10
        }
        sum = tmp_sum 
    }

    return sum
}