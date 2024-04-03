func isIsomorphic(s string, t string) bool {

    map_table_1 := make(map[uint8]uint8)
    map_table_2 := make(map[uint8]uint8)

    for i := 0; i < len(s); i++ {
        // s[i] and t[i] type are unit8
        if map_table_1[s[i]] == 0 && map_table_2[t[i]] == 0 {
            map_table_1[s[i]] = t[i]
            map_table_2[t[i]] = s[i]
            continue
        }

        if map_table_1[s[i]] != t[i] || map_table_2[t[i]] != s[i] {
            return false
        }
    }
    return true
}