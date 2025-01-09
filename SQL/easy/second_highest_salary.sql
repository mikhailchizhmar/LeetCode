-- https://leetcode.com/problems/second-highest-salary

SELECT
	CASE
		WHEN (SELECT COUNT(DISTINCT salary) FROM Employee) < 2 THEN NULL
		ELSE (
			SELECT DISTINCT salary
			FROM Employee
			ORDER BY salary DESC
			LIMIT 1 OFFSET 1
		)
	END AS SecondHighestSalary;

-- Easier solution:

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);