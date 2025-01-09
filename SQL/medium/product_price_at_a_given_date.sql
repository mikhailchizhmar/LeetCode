-- https://leetcode.com/problems/product-price-at-a-given-date

WITH p2 AS (
	SELECT product_id, MAX(change_date) AS latest_date
	FROM Products
	WHERE change_date <= '2019-08-16'
	GROUP BY product_id
)

SELECT DISTINCT product_id,
	CASE
		WHEN latest_date IS NOT NULL THEN new_price
		ELSE 10
	END AS price
FROM Products
LEFT JOIN p2 USING (product_id)
WHERE change_date = latest_date OR latest_date IS NULL
ORDER BY 1;

-- Solution with using UNION

(SELECT DISTINCT ON(product_id) product_id, new_price as price
FROM Products
WHERE change_date <= '2019-08-16'
ORDER BY product_id, change_date DESC)

UNION

(SELECT product_id, 10 AS price FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16');