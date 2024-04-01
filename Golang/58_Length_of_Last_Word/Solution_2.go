func lengthOfLastWord(s string) int {
    if len(s) < 1 {
        return 0
    }

    count := 0
    for i := len(s) -1; i>-1; i-- {
        if s[i] != ' ' {
            count += 1
        } else if count > 0 {
            return count
        }
    }
    return count
}