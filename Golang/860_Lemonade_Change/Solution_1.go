/*
Runtime 136 ms / Beats 5.47%
Memory 7.28 MB / Beats 98.44%
*/

func lemonadeChange(bills []int) bool {
    collection := make(map[int]int, 0)
    
    for _, bill := range bills {
        fmt.Println(bill, collection)
        collection[bill] += 1

        if bill == 10 {
            collection[5] -= 1
            if collection[5] < 0 {
                return false
            }
        } else if bill == 20 {
            if collection[5] > 0 && collection[10] > 0 {
                collection[5] -= 1
                collection[10] -= 1
            } else if collection[5] > 2 {
                collection[5] -= 3
            } else {
                return false
            }
        }
    }

    return true
}