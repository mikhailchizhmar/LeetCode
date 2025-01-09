-- https://leetcode.com/problems/fix-names-in-a-table

SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name)-1))) AS name
FROM users
ORDER BY 1;

SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM users
ORDER BY 1;

SELECT user_id, CONCAT(UPPER(SUBSTRING(name FROM 1 FOR 1)), LOWER(SUBSTRING(name FROM 2))) AS name
FROM users
ORDER BY 1;

SELECT user_id, INITCAP(name) AS name
FROM Users
ORDER BY 1;