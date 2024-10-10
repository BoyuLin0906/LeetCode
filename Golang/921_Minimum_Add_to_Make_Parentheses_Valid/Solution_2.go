func minAddToMakeValid(s string) int {

    open_brackets_count := 0 
    requried_adds_count := 0

    for _, char := range s {
        if char == '(' {
            open_brackets_count++
        } else {
            if open_brackets_count > 0 {
                open_brackets_count--
            } else {
                requried_adds_count++
            }
        }
    }

    return open_brackets_count + requried_adds_count
}