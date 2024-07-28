/*
Runtime 20 ms / Beats 34.69%
Memory 5.17 MB / Beats 40.82%
*/

// bellman-ford
func findTheCity(n int, edges [][]int, distanceThreshold int) int {
    cities_matrix := make([][]int, n)
    for i := 0; i < n; i++ {
        cities_matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            if i == j {
                cities_matrix[i][j] = 0
                continue
            }
            cities_matrix[i][j] = math.MaxInt
        }
    }

    for i := 0; i < n; i++ {
        bellmanFord(cities_matrix[i], edges , i)
    }

    return findMinRes(cities_matrix, n, distanceThreshold)
}


func bellmanFord(cities_matrix_row []int, edges [][]int, soruce int) {
   
    for i := 0; i < len(cities_matrix_row)-1; i++ {
        updated := false  
        for _, edge := range edges {
            from := edge[0]
            to := edge[1]
            weight := edge[2]
            if cities_matrix_row[from] != math.MaxInt && cities_matrix_row[to] > cities_matrix_row[from] + weight {
                cities_matrix_row[to] = cities_matrix_row[from] + weight
                updated = true
            } 

            if cities_matrix_row[to] != math.MaxInt && cities_matrix_row[from] > cities_matrix_row[to] + weight {
                cities_matrix_row[from] = cities_matrix_row[to] + weight
                updated = true
            }
        }
        
        if !updated {
            break
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