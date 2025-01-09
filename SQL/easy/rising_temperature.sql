-- https://leetcode.com/problems/rising-temperature

SELECT w1.id
FROM weather w1
JOIN weather w2 ON w2.recordDate = w1.recordDate - 1
WHERE w1.temperature > w2.temperature;