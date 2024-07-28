/*
Runtime 51 ms / Beats 20.00%
Memory 7.68 MB / Beats 10.61%
*/

// dijkstra
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
        dijkstra(cities_matrix[i], adjacency_list , i)
    }

    return findMinRes(cities_matrix, n, distanceThreshold)
}

type CityDistance struct {
    City     int 
    Distance int
}

type PriorityQueue []*CityDistance

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i].Distance < pq[j].Distance
}

func (pq *PriorityQueue) Swap(i, j int) {
    (*pq)[i], (*pq)[j] = (*pq)[j],  (*pq)[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
    item := x.(*CityDistance)
    *pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    old[n-1] = nil
    *pq = old[0 : n-1]
    return item
}


func dijkstra(cities_matrix_row []int, adjacency_list map[int]map[int]int, soruce int) {
    priority_queue := make(PriorityQueue, 0, len(cities_matrix_row))
    priority_queue = append(priority_queue, &CityDistance{City: soruce, Distance: 0})

    for len(priority_queue) > 0 {
        city_dis := heap.Pop(&priority_queue).(*CityDistance)
        curr_city := city_dis.City
        curr_distance := city_dis.Distance 
        if curr_distance > cities_matrix_row[curr_city] {
            continue
        }

        for next_city, next_weight := range adjacency_list[curr_city] {
            if cities_matrix_row[next_city] > next_weight + curr_distance {
                cities_matrix_row[next_city] = next_weight + curr_distance
                heap.Push(&priority_queue, &CityDistance{City: next_city, 
                                                         Distance: cities_matrix_row[next_city]})
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