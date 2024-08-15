/*
Runtime 86 ms / Beats 75.00%
Memory 8.07 MB / Beats 
52.34%
*/

func lemonadeChange(bills []int) bool {
    coin_5 := 0
    coin_10 := 0
    
    for _, bill := range bills {
        if bill == 5 {
            coin_5++

        } else if bill == 10 {
            coin_10++
            if coin_5 < 0 {
                return false
            }
            coin_5--

        } else if bill == 20 {
            if coin_5 > 0 && coin_10 > 0 {
                coin_5 -= 1
                coin_10 -= 1
            } else if coin_5 > 2 {
                coin_5 -= 3
            } else {
                return false
            }
        }
    }

    return true
}