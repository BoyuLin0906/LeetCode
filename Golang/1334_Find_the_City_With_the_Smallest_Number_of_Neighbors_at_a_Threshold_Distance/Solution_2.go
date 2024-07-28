/*
Runtime 108 ms / Beats 13.88%
Memory 7.01 MB / Beats 29.39%
*/

// SPFA offers a middle ground between Bellman-Ford and Dijkstra's algorithm

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

    adjacency_list := make(map[int]map[int]int)
    for i := 0; i < len(edges); i++ {
        from := edges[i][0]
        to := edges[i][1]
        weight := edges[i][2]

        if _, ok := adjacency_list[from]; !ok {
            adjacency_list[from] = make(map[int]int)
        }

        if _, ok := adjacency_list[to]; !ok {
            adjacency_list[to] = make(map[int]int)
        }

        adjacency_list[from][to] = weight
        adjacency_list[to][from] = weight
    }

    for i := 0; i < n; i++ {
        spfa(cities_matrix[i], adjacency_list , i)
    }

    return findMinRes(cities_matrix, n, distanceThreshold)
}


func spfa(cities_matrix_row []int, adjacency_list map[int]map[int]int, soruce int) {
    queue := make([]int, 0, len(cities_matrix_row))
    queue = append(queue, soruce)

    for len(queue) > 0 {
        curr_city := queue[0]
        queue = queue[1:]
        curr_distance := cities_matrix_row[curr_city]
        for next_city, next_weight := range adjacency_list[curr_city] {
            if cities_matrix_row[next_city] > next_weight + curr_distance {
                cities_matrix_row[next_city] = next_weight + curr_distance
                queue = append(queue, next_city)
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