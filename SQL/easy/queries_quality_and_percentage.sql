-- https://leetcode.com/problems/queries-quality-and-percentage

SELECT query_name,
       ROUND(SUM(rating::numeric / position) / COUNT(result), 2) AS quality,
       ROUND(100. * COUNT(rating) FILTER (WHERE rating < 3) / COUNT(rating), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;