-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports

WITH
    managerIDs AS (
        SELECT managerId
        FROM Employee
        GROUP BY managerId
        HAVING COUNT(managerId) >= 5
    )

SELECT e.name
FROM Employee e
JOIN managerIDs m ON m.managerId = e.id;
