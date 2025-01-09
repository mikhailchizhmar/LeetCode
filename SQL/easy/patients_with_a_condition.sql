-- https://leetcode.com/problems/patients-with-a-condition

SELECT * FROM patients
WHERE conditions ~ '(^| )DIAB1';