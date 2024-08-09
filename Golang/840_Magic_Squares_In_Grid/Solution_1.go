/*
Runtime 2 ms / Beats 56.25%
Memory 2.85 MB / Beats 6.25%
*/

type Square struct {
    LCol       int
    MCol       int
    RCol       int
    TRow       int
    MRow       int
    DRow       int
    LRDiagonal int
    RLDiagonal int
    Seen       []int
}

func numMagicSquaresInside(grid [][]int) int {
    row_len := len(grid)
    col_len := len(grid[0])
    
    if row_len < 3 || col_len < 3 {
        return 0
    }

    sum_grid := make([][]*Square, row_len-2)
    for i := 0; i < row_len-2; i++ {
        sum_grid[i] = make([]*Square, col_len-2)
    }

    seen := make([]int, 16)
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            seen[grid[i][j]]++
        }
    }
    sq := &Square{LCol: grid[0][0] + grid[1][0] + grid[2][0],
                  MCol: grid[0][1] + grid[1][1] + grid[2][1],
                  RCol: grid[0][2] + grid[1][2] + grid[2][2],
                  TRow: grid[0][0] + grid[0][1] + grid[0][2],
                  MRow: grid[1][0] + grid[1][1] + grid[1][2],
                  DRow: grid[2][0] + grid[2][1] + grid[2][2],
                  LRDiagonal: grid[0][0] + grid[1][1] + grid[2][2],
                  RLDiagonal: grid[0][2] + grid[1][1] + grid[2][0],
                  Seen: seen}

    sum_grid[0][0] = sq

    res := 0
    if check_squera(sum_grid[0][0]) {
        res++
    }

    for i := 0; i < row_len-2; i++ {
        if i != 0 {
            down_seen := make([]int, 16)
            copy(down_seen, sum_grid[i-1][0].Seen)
            for k := 0; k < 3; k++ {
                down_seen[grid[i-1][k]]--
                down_seen[grid[i+2][k]]++
            }
            down_sq := &Square{LCol: sum_grid[i-1][0].LCol - grid[i-1][0] + grid[i+2][0],
                               MCol: sum_grid[i-1][0].MCol - grid[i-1][1] + grid[i+2][1],
                               RCol: sum_grid[i-1][0].RCol - grid[i-1][2] + grid[i+2][2],
                               TRow: sum_grid[i-1][0].MRow,
                               MRow: sum_grid[i-1][0].DRow,
                               DRow: grid[i+2][0] + grid[i+2][1] + grid[i+2][2],
                               LRDiagonal: grid[i][0] + grid[i+1][1] + grid[i+2][2],
                               RLDiagonal: grid[i][2] + grid[i+1][1] + grid[i+2][0],
                               Seen: down_seen}
            sum_grid[i][0] = down_sq
            if check_squera(sum_grid[i][0]) {
                res++
            }
        }
       
        for j := 1; j < col_len-2; j++ {
            right_seen := make([]int, 16)
            copy(right_seen, sum_grid[i][j-1].Seen)
            for k := 0; k < 3; k++ {
                right_seen[grid[i+k][j-1]]--
                right_seen[grid[i+k][j+2]]++
            }
            right_sq := &Square{LCol: sum_grid[i][j-1].MCol, 
                                MCol: sum_grid[i][j-1].RCol,
                                RCol: grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2],
                                TRow: sum_grid[i][j-1].TRow - grid[i][j-1] + grid[i][j+2],
                                MRow: sum_grid[i][j-1].MRow - grid[i+1][j-1] + grid[i+1][j+2],
                                DRow: sum_grid[i][j-1].DRow - grid[i+2][j-1] + grid[i+2][j+2],
                                LRDiagonal: grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2],
                                RLDiagonal: grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j],
                                Seen: right_seen}
            sum_grid[i][j] = right_sq
            if check_squera(sum_grid[i][j]) {
                res++
            }
        }
    }
    return res
}

func check_squera(sq *Square) bool {
    if sq.LCol != 15 || sq.MCol != 15 || sq.RCol != 15 {
        return false
    }
    if sq.TRow != 15 || sq.MRow != 15 || sq.DRow != 15 {
        return false
    }
    if sq.LRDiagonal != 15 || sq.RLDiagonal != 15 {
        return false
    }
    for i := 1; i < 10; i++ {
        if sq.Seen[i] <= 0 {
            return false
        }
    }
    return true
}