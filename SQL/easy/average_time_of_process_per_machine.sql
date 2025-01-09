-- https://leetcode.com/problems/average-time-of-process-per-machine

SELECT machine_id, ROUND(
    (SUM(timestamp) FILTER (WHERE activity_type = 'end') - SUM(timestamp) FILTER (WHERE activity_type = 'start')
    )::numeric / COUNT(DISTINCT process_id), 3) AS processing_time
FROM Activity
GROUP BY machine_id