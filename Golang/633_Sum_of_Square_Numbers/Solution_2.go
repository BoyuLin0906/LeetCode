/*
Runtime 40 ms / Beats 31.03%
Memory 2.20 MB / Beats 72.41%
*/

func judgeSquareSum(c int) bool {
    
    for val_a := 0; val_a * val_a <= c; val_a++ {
        val_b := c - val_a * val_a
        
        right := val_b
        left := 0
        for left <= right {
            mid := left + (right - left) / 2;
            
            if mid * mid == val_b {
                return true
            }
            
            if mid * mid > val_b {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
    }
    return false
}