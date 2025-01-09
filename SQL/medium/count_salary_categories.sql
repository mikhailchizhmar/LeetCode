-- https://leetcode.com/problems/count-salary-categories

-- Solution with using UNNEST
SELECT 
    UNNEST(ARRAY['Low Salary', 'Average Salary', 'High Salary']) AS category,
    UNNEST(ARRAY[
        COUNT(*) FILTER (WHERE income < 20000),
        COUNT(*) FILTER (WHERE income BETWEEN 20000 AND 50000), 
        COUNT(*) FILTER (WHERE income > 50000)
    ]) AS accounts_count
FROM Accounts

-- time limit exceeded
SELECT 'Low Salary' as category, COUNT(*) FILTER (WHERE income < 20000) AS accounts_count
FROM Accounts
UNION
SELECT 'Average Salary' as category, COUNT(*) FILTER (WHERE income BETWEEN 20000 AND 50000)
FROM Accounts
UNION
SELECT 'High Salary' as category, COUNT(*) FILTER (WHERE income > 50000)
FROM Accounts

-- time limit exceeded
WITH cte AS (
	SELECT *,
		CASE
			WHEN income < 20000 THEN 'Low Salary'
			WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
			ELSE 'High Salary'
		END AS category
	FROM accounts),
categories AS (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
)

SELECT c.category, COALESCE(COUNT(cte.category), 0) AS accounts_count
FROM categories c
LEFT JOIN cte ON c.category = cte.category
GROUP BY c.category;
