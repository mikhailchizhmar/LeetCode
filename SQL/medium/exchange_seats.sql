-- https://leetcode.com/problems/exchange-seats

SELECT id,
	COALESCE(
		CASE
			WHEN id % 2 != 0 THEN lead
			ELSE lag
		END,
		student) AS student
FROM (
	SELECT *, LAG(student) OVER (ORDER BY id), LEAD(student) OVER (ORDER BY id)
	FROM Seat
);

-- Without window functions:

SELECT s1.id,
	COALESCE(
		CASE
			WHEN s1.id % 2 != 0 THEN s2.student
			ELSE s3.student
		END,
		s1.student) AS student
FROM Seat s1
LEFT JOIN Seat s2 ON s1.id = s2.id - 1
LEFT JOIN Seat s3 ON s1.id = s3.id + 1

-- Easier solution:

SELECT
    CASE
        WHEN id % 2 = 1 AND  id = (SELECT MAX(id) FROM Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
    END AS id,
    student 
FROM Seat
ORDER BY id
