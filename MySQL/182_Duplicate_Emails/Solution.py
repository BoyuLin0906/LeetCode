# Write your MySQL query statement below
# WHERE: filter before getting values
# HAVING: filter after getting values
SELECT email 
    FROM Person 
    GROUP BY email
    HAVING COUNT(*) > 1