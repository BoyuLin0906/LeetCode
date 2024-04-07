func maximumOddBinaryNumber(s string) string {

    count := 0
    for _, bit := range s {
        if bit == '1' {
            count++
        }
    }

    count --
    res := ""
    for i := 0; i < len(s)-1; i++ {
        if count > 0 {
            res =  res + "1"
            count --
        } else {
            res = res + "0"  
        }
    } 
    return res + "1"
}