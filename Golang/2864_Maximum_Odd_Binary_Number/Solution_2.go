func maximumOddBinaryNumber(s string) string {

    part_1 := strings.Repeat("1", strings.Count(s, "1")-1) 
    part_2 := strings.Repeat("0", strings.Count(s, "0"))
    return part_1 + part_2 + "1"
}