/*
Runtime 76 ms / Beats 100.00%
Memory 8.52 MB / Beats 66.67%
*/

func minDays(bloomDay []int, m int, k int) int {
    if len(bloomDay) < m * k {
        return -1
    }

    left := 1
    right := slices.Max(bloomDay)
    for left <= right {
        middle := (left + right)/2
        bouquets := getBouquet(bloomDay, middle, k)
        if bouquets < m {
            left = middle + 1
        } else {
            right = middle - 1
        }
    }
    return left
}

func getBouquet(bloom_day []int, threshold int, adjacent_flowers int) int {
    count := 0
    cur_bloom_flower := 0
    for _, day := range bloom_day {
        if day > threshold {
            cur_bloom_flower = 0
            continue
        }

        cur_bloom_flower += 1
        if cur_bloom_flower == adjacent_flowers {
            count += 1
            cur_bloom_flower = 0
        }
    }
    return count
}