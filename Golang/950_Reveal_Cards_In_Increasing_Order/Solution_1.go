/*
Runtime 3 ms / Beats 86.96%
Memory 3.07 MB / Beats 91.30%
*/

func deckRevealedIncreasing(deck []int) []int {

    sort.Ints(deck)
    deck_len := len(deck)
    res := make([]int, deck_len)
    reveal := true

    for len(deck) > 0 {
        for i := 0; i < deck_len; i++ {
            if res[i] == 0{
                if reveal {
                    res[i] = deck[0]
                    deck = deck[1:len(deck)]
                    reveal = false
                } else {
                    reveal = true
                    continue
                }
            }
        }
    }

    return res
}