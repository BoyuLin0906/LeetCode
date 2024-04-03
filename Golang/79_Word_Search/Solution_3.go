func exist(board [][]byte, word string) bool {
    /*
    Runtime 102 ms / Beats 82.53%
    Memory 2.16 MB / Beats 54.18%
    */
    height := len(board)
    width := len(board[0])

    for i := 0; i < height; i++ {
        for j := 0; j < width; j++ {
            if find_word(board, word, 0, j, i, width, height) {
                return true
            }
        }
    }
    return false
}

func find_word(board [][]byte, word string, index int, x int, y int, width int, height int) bool {
    if x < 0 || x >= width || y < 0 || y >= height || board [y][x] == 0 {
        return false
    }

    if board[y][x] != word[index] {
        return false
    }

    temp := board[y][x]
    board[y][x] = 0;

    if len(word)-1 == index {
        return true
    }

    index += 1
    if find_word(board, word, index, x+1, y, width, height) {
        return true
    }
    if find_word(board, word, index, x-1, y, width, height) {
        return true
    }
    if find_word(board, word, index, x, y+1, width, height) {
        return true
    }
    if find_word(board, word, index, x, y-1, width, height) {
        return true
    }
    board[y][x] = temp
    
    return false
}