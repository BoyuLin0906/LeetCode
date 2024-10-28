/*
Runtime 3 ms / Beats 77.36%
Memory 4.32 MB / Beats 81.13%
*/

func shortestPalindrome(s string) string {
    if len(s) == 0 {
        return s
    }
    
    left_idx := 0
    for right_idx := len(s)-1; right_idx >= 0; right_idx-- {
        if s[left_idx] == s[right_idx] {
            left_idx++
        }
    }

    if left_idx == len(s) {
        return s
    }
    
    non_palindrome_suffix := s[left_idx:]
    reverse_suffix := reverseString(non_palindrome_suffix)
    return reverse_suffix + shortestPalindrome(s[:left_idx]) + non_palindrome_suffix
}

func reverseString(s string) string {
    runes := []rune(s)

    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}