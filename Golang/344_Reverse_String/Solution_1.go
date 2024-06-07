/*
Runtime 28 ms / Beats 74.56%
Memory 6.70 MB / Beats 68.41%
*/

func reverseString(s []byte)  {
    i, j := 0, len(s)-1
    
    for i < j {
        s[i], s[j] = s[j], s[i]
        i++
        j--
    }
}