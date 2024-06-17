/*
Runtime 3 ms / Beats 62.07%
Memory 2.19 MB / Beats 72.41%
*/

func judgeSquareSum(c int) bool {
    
    for val_a := 0; val_a * val_a <= c; val_a++ {
        val_b := c - val_a * val_a
        
        val := int(math.Sqrt(float64(val_b)))
        if val * val == val_b {
            return true
        }
    }
    return false
}