func countStudents(students []int, sandwiches []int) int {
    queue_len := len(students)

    student_square_count := 0
    student_circular_count := 0
    sandwich_square_count := 0

    for i := 0 ; i < queue_len ; i++ {
        if students[i] == 1 {
            student_square_count++
        } else {
            student_circular_count++
        }

        if sandwiches[i] == 1 {
            sandwich_square_count++
        }
    }

    if student_square_count == sandwich_square_count {
        return 0
    }

    for i := 0 ; i < queue_len ; i++ {
        if (sandwiches[i] == 0 && student_circular_count == 0) || 
           (sandwiches[i] == 1 && student_square_count == 0) {
            break
        }

        if sandwiches[i] == 1 {
            student_square_count--
        } else {
            student_circular_count--
        }
    }

    return student_square_count + student_circular_count
}