/*
Runtime 1 ms / Beats 72.15%
Memory 2.38 MB / Beats 40.51%
*/

func countStudents(students []int, sandwiches []int) int {

    last_served_count := 0
    for len(students) > 0 && last_served_count < len(students) {
        if sandwiches[0] == students[0] {
            sandwiches = sandwiches[1:len(sandwiches)]
            students = students[1:len(students)]
            last_served_count = 0
        } else {
            student := students[0]
            students = append(students[1:len(students)], student)
            last_served_count++
        }
    }
    return len(students)
}