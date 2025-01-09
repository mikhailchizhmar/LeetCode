-- https://leetcode.com/problems/primary-department-for-each-employee

SELECT employee_id, department_id
FROM (
	SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS cnt_deps
	FROM Employee
)
WHERE primary_flag = 'Y' OR cnt_deps = 1

-- Another solution

SELECT employee_id, department_id 
FROM Employee
WHERE employee_id IN (
	SELECT employee_id 
	FROM Employee
	GROUP BY employee_id 
	HAVING COUNT(*) = 1
) OR primary_flag = 'Y'