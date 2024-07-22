/*
Runtime 17 ms / Beats 84.04%
Memory 7.76 MB / Beats 10.64%
*/

type People struct {
    name string
    height int
}

func sortPeople(names []string, heights []int) []string {
    
    people_struct := make([]*People, len(names))
    for i := 0; i < len(names); i++ {
        people_struct[i] = &People{name: names[i], height: heights[i]}
    }

    sort.Slice(people_struct, func(i, j int) bool {
		return people_struct[i].height > people_struct[j].height
	})

    for i := 0; i < len(names); i++ {
       names[i] = people_struct[i].name
    }
    return names
}