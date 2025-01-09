-- https://leetcode.com/problems/students-and-examinations

SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e USING(student_id, subject_name)
GROUP BY 1, 2, 3
ORDER BY 1, 3;