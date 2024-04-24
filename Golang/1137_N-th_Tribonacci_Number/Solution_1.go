/*
Runtime 0 ms / Beats 100.00%
Memory 2.12 MB / Beats 32.67%
*/

func tribonacci(n int) int {
    if n == 0 {
        return 0
    }
    if n == 1 || n == 2{
        return 1
    }
    num1 := 0
    num2 := 1
    num3 := 1
    temp := 0

    for i := 3; i <= n; i++ {
        temp = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = temp
    }
    return temp
}