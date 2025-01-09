-- https://leetcode.com/problems/consecutive-numbers

SELECT DISTINCT num AS ConsecutiveNums
FROM (
	SELECT 
		*,
		LAG(num) OVER (ORDER BY id) AS lag1,
		LAG(num, 2) OVER (ORDER BY id) AS lag2
	FROM Logs
)
WHERE num = lag1 AND num = lag2;

-- Another solution

SELECT DISTINCT l1.num ConsecutiveNums
FROM Logs l1
LEFT JOIN Logs l2 ON l1.id = l2.id + 1
LEFT JOIN Logs l3 ON l1.id = l3.id + 2
WHERE l1.num = l2.num AND l2.num = l3.num;