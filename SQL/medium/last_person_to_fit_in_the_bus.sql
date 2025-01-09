-- https://leetcode.com/problems/last-person-to-fit-in-the-bus

SELECT person_name
FROM (
	SELECT *, SUM(weight) OVER (ORDER BY turn) AS total_weight
	FROM queue 
	ORDER BY turn
)
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;


-- Recursive solution:

--1)  Use Recursion to generate a "weights" table
--1a) Base query will select the first person (turn = 1)
--1b) Recursive query (union query) will be increasing by 1 starting at n + 1. This query utilizes a JOIN to get the next person's information (join weights.n + 1 to Queue.turn)
--1c) WHERE stops after total weight exceeds or equals 1000
--2)  Select the last person by ordering descendingly the table created recursive query created in 1) with a limit 1
WITH RECURSIVE weights AS (
    SELECT
        turn,
        person_name,
        weight,
        weight AS total_weight,
        1 as n
    FROM
        Queue q
    WHERE
        turn = 1
    UNION
    SELECT
        q.turn,
        q.person_name,
        q.weight,
        w.total_weight + q.weight AS total_weight,
        n + 1 as n
    FROM
        weights w
    JOIN
        Queue q
    ON
        w.n + 1 = q.turn
    WHERE
        w.total_weight + q.weight <= 1000
)

SELECT person_name
FROM weights
ORDER BY total_weight DESC
LIMIT 1;