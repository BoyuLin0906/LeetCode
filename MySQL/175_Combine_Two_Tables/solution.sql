# Write your MySQL query statement below
/*
Runtime: 333 ms, faster than 90.56% of MySQL online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.
*/
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address 
ON Person.personId = Address.personId