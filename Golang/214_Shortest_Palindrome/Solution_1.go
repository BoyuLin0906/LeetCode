/*
Runtime 3 ms / Beats 77.36%
Memory 4.29 MB / Beats 90.57%
*/

func shortestPalindrome(s string) string {
    reverse_s := reverseString(s)

    for i := 0; i < len(s); i++ {
        if s[:len(s)-i] == reverse_s[i:] {
            return reverse_s[:i] + s 
        }
    }

    return ""
}

func reverseString(s string) string {
    runes := []rune(s)

    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}