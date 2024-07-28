/*
Runtime 8 ms / Beats 95.10%
Memory 4.74 MB / Beats 49.39%
*/

// floyd
func findTheCity(n int, edges [][]int, distanceThreshold int) int {
    cities_matrix := make([][]int, n)
    for i := 0; i < n; i++ {
        cities_matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            if i == j {
                cities_matrix[i][j] = 0
                continue
            }
            cities_matrix[i][j] = 10001
        }
    }

    for i := 0; i < len(edges); i++ {
        from := edges[i][0]
        to := edges[i][1]
        weight := edges[i][2]

        cities_matrix[from][to] = weight
        cities_matrix[to][from] = weight
    }
    
    floyd(cities_matrix, n)
    return findMinRes(cities_matrix, n, distanceThreshold)
}

func floyd(matrix [][]int, n int) {
    for k := 0; k < n; k ++ {
        for i := 0; i < n; i ++ {
            for j := 0; j < n; j ++ {
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
            }
        }
    }
}

func findMinRes(cities_matrix [][]int, cities_amount int, threshold int) int {
    min_reachable_count := cities_amount
    res_city := -1 
    for i := cities_amount-1; i > -1; i-- {
        count := 0
  
        for _, val := range cities_matrix[i] {
            if val <= threshold && val != 0{
                count++
            }
        }
 
        if min_reachable_count > count {
            min_reachable_count = count
            res_city = i
        }
    } 

    return res_city
}