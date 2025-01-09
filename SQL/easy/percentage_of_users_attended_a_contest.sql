-- https://leetcode.com/problems/percentage-of-users-attended-a-contest

SELECT r.contest_id, ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM users), 2) AS percentage
FROM users u
JOIN register r USING(user_id)
GROUP BY r.contest_id
ORDER BY 2 DESC, 1;