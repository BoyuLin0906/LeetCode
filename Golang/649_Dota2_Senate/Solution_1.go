/*
Runtime 0 ms / Beats 100.00%
Memory 4.06 MB / Beats 63.40%
*/

func predictPartyVictory(senate string) string {

    radiant := make([]int, 0, len(senate))
    dire := make([]int, 0, len(senate))
    
    for idx, party := range senate {
        if party == 'R' {
            radiant = append(radiant, idx)
        } else {
            dire = append(dire, idx)
        }
    }

    for len(radiant) > 0 && len(dire) > 0 {
        if radiant[0] < dire[0] {
            radiant = append(radiant, radiant[0] + len(senate))
        } else {
            dire = append(dire, dire[0] + len(senate))
        }
        fmt.Println(radiant, dire)
        radiant = radiant[1:]
        dire = dire[1:]
    }

    if len(radiant) > 0 {
        return "Radiant"
    }
    return "Dire"
}