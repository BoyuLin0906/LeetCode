func exist(board [][]byte, word string) bool {
    /*
    Runtime 1409 ms / Beats 5.06%
    Memory 23.00 MB / Beats 5.06%
    */
    height := len(board)
    width := len(board[0])

    for i := 0; i < height; i++ {
        for j := 0; j < width; j++ {
            if find_word(board, word, j, i, width, height) {
                return true
            }
        }
    }
    return false
}

func find_word(board [][]byte, word string, x int, y int, width int, height int) bool {

    current_char := byte(word[0])
    if current_char == board[y][x] {
        next_word_pattern := word[1:]
        new_board := make([][]byte, height)
        copy_two_dim_byte_map(board, new_board, width, height)
        new_board[y][x] = 0;

        if len(next_word_pattern) == 0 {
            return true
        }

        if x < width-1 {
            if find_word(new_board, next_word_pattern, x+1, y, width, height) {
                return true
            }
        }
        if x > 0 {
            if find_word(new_board, next_word_pattern, x-1, y, width, height) {
                return true
            }
        }
        if y < height-1 {
            if find_word(new_board, next_word_pattern, x, y+1, width, height) {
                return true
            }
        } 
        if y > 0 {
            if find_word(new_board, next_word_pattern, x, y-1, width, height) {
                return true
            }
        }
    }
    return false
}

func copy_two_dim_byte_map(old [][]byte, new [][]byte, width int, height int) {
    for i := 0; i < height; i++ {
        new[i] = make([]byte, width)
        for j := 0; j < width; j++ {
            new[i][j] = old[i][j]
        }
    }
}