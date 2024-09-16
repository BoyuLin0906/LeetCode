/*
Runtime 541 ms / Beats 5.63%
Memory 5.56 MB / Beats 16.90%
*/

func findMinDifference(timePoints []string) int {
    intTimePoints := convertTimeToMinute(timePoints)

    min_val := math.MaxInt
    for i := 0; i < len(timePoints); i++ {
        for j := i+1; j < len(timePoints); j++ {
            min_val = min(min_val, abs(intTimePoints[j]-intTimePoints[i]))
            if intTimePoints[j] > intTimePoints[i] {
                min_val = min(min_val, (intTimePoints[i]+1440) - intTimePoints[j])
            } else {
                min_val = min(min_val, (intTimePoints[j]+1440) - intTimePoints[i])
            }
        }
    }
    return min_val
}

func convertTimeToMinute(timePoints []string) []int {
    intTimePoints := make([]int, len(timePoints))
    for i := 0; i < len(timePoints); i++ {
        intTimePoints[i] = getMinute(timePoints[i])
    }
    return intTimePoints
}

func getMinute(time string) int {
    split_time := strings.Split(time, ":")
    hour, _ := strconv.Atoi(split_time[0])
    minute, _ := strconv.Atoi(split_time[1])
    return hour * 60 + minute
}

func abs(val int) int {
    if val < 0 {
        return -val
    }
    return val
}