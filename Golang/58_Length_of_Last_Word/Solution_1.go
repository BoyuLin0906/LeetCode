func lengthOfLastWord(s string) int {
    s = strings.TrimRight(s, " ")
    s_slice := strings.Split(s, " ")
    word := s_slice[len(s_slice)-1]
    return len(word)
}