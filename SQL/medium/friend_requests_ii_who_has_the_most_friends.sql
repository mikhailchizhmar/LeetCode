-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends

WITH cte AS (
    (SELECT requester_id AS id FROM RequestAccepted)
    UNION ALL
    (SELECT accepter_id FROM RequestAccepted)
)

SELECT id, COUNT(*) AS num
FROM cte
GROUP BY id
ORDER BY 2 DESC
LIMIT 1;