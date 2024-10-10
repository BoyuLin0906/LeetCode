/*
Runtime 0 ms / Beats 100.00%
Memory 3.71 MB / Beats 33.38%
*/

func isValidSudoku(board [][]byte) bool {
    
    checked_row := make([]map[byte]bool, 9)
    checked_col := make([]map[byte]bool, 9)
    checked_sub_box := make([]map[byte]bool, 9)

    for idx := 0; idx < 9; idx++ {
        checked_row[idx] = make(map[byte]bool, 0)
        checked_col[idx] = make(map[byte]bool, 0)
        checked_sub_box[idx] = make(map[byte]bool, 0)
    }

    for row_idx := 0; row_idx < 9; row_idx++ {
        for col_idx := 0; col_idx < 9; col_idx++ {
            
            digit := board[row_idx][col_idx]
            if digit == '.' {
                continue
            } 

            if checked_row[row_idx][digit] {
                return false
            }
            checked_row[row_idx][digit] = true

            if checked_col[col_idx][digit] {
                return false
            }
            checked_col[col_idx][digit] = true

            sub_box_row := row_idx / 3
            sub_box_col := col_idx / 3
            sub_box_idx := sub_box_row + sub_box_col*3
            if checked_sub_box[sub_box_idx][digit] {
                return false
            }
            checked_sub_box[sub_box_idx][digit] = true
        }
    }

    return true
}