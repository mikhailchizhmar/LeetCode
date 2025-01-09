-- https://leetcode.com/problems/movie-rating

(SELECT u.name AS results
FROM MovieRating mr
JOIN Users u USING(user_id)
GROUP BY u.name
ORDER BY COUNT(*) DESC, 1
LIMIT 1)

UNION ALL

(SELECT m.title
FROM MovieRating mr
JOIN Movies m USING(movie_id)
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
-- WHERE TO_CHAR(created_at,'YYYY-MM') = '2020-02'
GROUP BY m.title
ORDER BY AVG(rating) DESC, 1
LIMIT 1)
