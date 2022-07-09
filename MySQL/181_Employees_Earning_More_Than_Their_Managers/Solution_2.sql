# Write your MySQL query statement below
/*
Runtime: 368 ms, faster than 75.22% of MySQL online submissions for Employees Earning More Than Their Managers.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
*/
SELECT 
  Employee_a.name AS Employee 
FROM 
  Employee AS Employee_a JOIN Employee AS Employee_b
  ON Employee_a.ManagerId = Employee_b.id
WHERE 
  Employee_a.Salary > Employee_b.Salary