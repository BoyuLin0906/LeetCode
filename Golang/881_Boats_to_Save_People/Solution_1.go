/*
Runtime 54 ms / Beats 80.23%
Memory 6.97 MB / Beats 90.70%
*/


func numRescueBoats(people []int, limit int) int {
    
    sort.Ints(people)
    left := 0
    right := len(people)-1
    res := 0

    for left < right {
        if people[left] + people[right] <= limit {
            left++
            res++
        } else {
            res++
        }
        right--
    }
    
    if left == right {
        res++
    }
    
    return res
}