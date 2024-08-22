/*
Runtime 0 ms / Beats 100.00%
Memory 2.17 MB / Beats 67.06%
*/

func findComplement(num int) int {
    
    tmp := num
    mask := 1
    for tmp > 0 {
        num ^= val
        mask = val << 1
        tmp = tmp >> 1
    }

    return num
}