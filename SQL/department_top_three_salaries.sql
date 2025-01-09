-- https://leetcode.com/problems/department-top-three-salaries

SELECT
	Department,
	Employee,
	Salary
FROM (
	SELECT
		e.name AS Employee,
		e.salary AS Salary,
		d.name AS Department,
		DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC)
	FROM Employee e
	JOIN Department d ON e.departmentId = d.id
)
WHERE dense_rank <= 3
ORDER BY Department, Salary DESC;

-- Solution without window functions:

SELECT d.name AS Department, e.name AS Employee, salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE salary IN (
    SELECT DISTINCT(salary)
    FROM Employee
    WHERE Employee.departmentId = d.id
    ORDER BY salary DESC
    LIMIT 3
)