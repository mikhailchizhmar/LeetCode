-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions

SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM visits v
LEFT JOIN transactions t USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY v.customer_id
ORDER BY 2 DESC;