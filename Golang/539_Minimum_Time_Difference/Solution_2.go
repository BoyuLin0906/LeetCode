/*
Runtime 0 ms / Beats 100.00%
Memory 4.73 MB / Beats 43.66%
*/

func findMinDifference(timePoints []string) int {
    minute_tables := make(map[int]bool)
    max_time := 0
    min_time := 60 * 24

    for _, time := range timePoints {
        minute_time := getMinute(time)
        min_time = min(min_time, minute_time)
        max_time = max(max_time, minute_time)
        
        if minute_tables[minute_time] {
            return 0
        }
        minute_tables[minute_time] = true
    }

    prev := min_time
    res := 1440 - max_time + min_time
    for i := min_time+1; i <= max_time; i++ {
        if minute_tables[i] {
            diff := i - prev
            if diff < res {
                res = diff
            }
            prev = i
        }
    }

    return res
}

func getMinute(time string) int {
    split_time := strings.Split(time, ":")
    hour, _ := strconv.Atoi(split_time[0])
    minute, _ := strconv.Atoi(split_time[1])
    return hour * 60 + minute
}