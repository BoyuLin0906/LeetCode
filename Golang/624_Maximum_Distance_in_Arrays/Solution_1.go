/*
Runtime 188 ms / Beats 84.00%
Memory 13.30 MB / Beats 80.00%
*/

func maxDistance(arrays [][]int) int {
    max_dis := 0
    cur_min := arrays[0][0]
    cur_max := arrays[0][len(arrays[0])-1]
    for i := 1; i < len(arrays); i++ {
        diff_1 := abs(cur_min - arrays[i][len(arrays[i])-1])
        diff_2 := abs(cur_max - arrays[i][0])
        max_dis = max(max_dis, diff_1, diff_2)
        cur_max = max(cur_max, arrays[i][len(arrays[i])-1])
        cur_min = min(cur_min, arrays[i][0])
    }
    return max_dis
}

func abs(num int) int {
    if num < 0 {
        return -num
    }
    return num
}