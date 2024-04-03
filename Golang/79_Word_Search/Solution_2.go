func exist(board [][]byte, word string) bool {
    /*
    Runtime 103 ms / Beats 81.01%
    Memory 2.31 MB / Beats 27.09%
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
    if x < 0 || x >= width || y < 0 || y >= height || board [y][x] == 0 {
        return false
    }

    current_char := byte(word[0])
    if current_char != board[y][x] {
        return false
    }

    next_word_pattern := word[1:]
    temp := board[y][x]
    board[y][x] = 0;

    if len(next_word_pattern) == 0 {
        return true
    }

    res_1 := find_word(board, next_word_pattern, x+1, y, width, height)
    res_2 := find_word(board, next_word_pattern, x-1, y, width, height)
    res_3 := find_word(board, next_word_pattern, x, y+1, width, height)
    res_4 := find_word(board, next_word_pattern, x, y-1, width, height)
    board[y][x] = temp
    
    return res_1 || res_2 || res_3 || res_4
}