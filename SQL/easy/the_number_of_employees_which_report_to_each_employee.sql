-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee

-- Beautiful solution

SELECT e1.employee_id, MIN(e1.name) AS name, COUNT(e2.reports_to) AS reports_count, ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
JOIN Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
ORDER BY 1;

-- Brute force

WITH cte AS (
    SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM Employees
    GROUP BY reports_to
    HAVING reports_to IS NOT NULL
)

SELECT e.employee_id, e.name, reports_count, average_age
FROM Employees e
JOIN cte ON e.employee_id = cte.reports_to
ORDER BY 1;