# Write your MySQL query statement below
/*
Runtime: 533 ms, faster than 36.50% of MySQL online submissions for Employees Earning More Than Their Managers.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.
*/
SELECT 
  Employee_a.name AS Employee 
FROM 
  Employee AS Employee_a,
  Employee AS Employee_b
WHERE 
  Employee_a.ManagerId = Employee_b.id
  AND Employee_a.Salary > Employee_b.Salary