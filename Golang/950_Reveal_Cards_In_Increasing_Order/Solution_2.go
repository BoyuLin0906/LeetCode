/*
Runtime 3 ms / Beats 86.96%
Memory 3.34 MB / Beats 43.48%
*/

func deckRevealedIncreasing(deck []int) []int {

    sort.Ints(deck)
    deck_len := len(deck)
    
    index_queue := make([]int, deck_len)
    for i, _ := range deck {
        index_queue[i] = i
    }

    res := make([]int, deck_len)
    for _, card := range deck {
        res[index_queue[0]] = card
        index_queue = index_queue[1:len(index_queue)]

        if len(index_queue) > 0 {
            index_queue = append(index_queue[1:len(index_queue)], index_queue[0])
        }
    }

    return res
}