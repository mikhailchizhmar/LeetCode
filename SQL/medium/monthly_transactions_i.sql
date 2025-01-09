-- https://leetcode.com/problems/monthly-transactions-i

SELECT 
	TO_CHAR(trans_date, 'YYYY-MM') AS month, 
	country, 
	COUNT(*) AS trans_count, 
	COALESCE(COUNT(*) FILTER (WHERE state = 'approved'), 0) AS approved_count,
	SUM(amount) AS trans_total_amount,
	COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount
FROM Transactions
GROUP BY "month", country;