-- https://leetcode.com/problems/find-users-with-valid-e-mails

SELECT *
FROM Users
WHERE mail ~ '^[a-zA-Z]+[\w\-_\.]*@leetcode\.com$';