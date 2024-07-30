/*
Runtime 32 ms / Beats 44.44%
Memory 6.99 MB / Beats 72.22%
*/

func minimumDeletions(s string) int {
    stack := make([]rune, 0, len(s))
    popped_a := 0
    right_b := 0

    for _, char := range s {
        if len(stack) > 0 && stack[len(stack)-1] == 'b' && char == 'a' {
            if popped_a + 1 > right_b {
                stack = stack[:len(stack)-right_b]
                right_b = 0
                
                for i := 0; i < popped_a + 1; i++ {
                    stack = append(stack, 'a')
                }
                popped_a = 0
            } else {
                popped_a++
            }
            continue
        }
        
        if char == 'b' {
            right_b++
        }
        stack = append(stack, char)
    }

    return len(s) - len(stack)
}