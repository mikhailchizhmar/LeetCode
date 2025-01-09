-- https://leetcode.com/problems/customers-who-bought-all-products

-- Here we make sure that Customer table contains only values that are presented in Product table

SELECT customer_id
FROM (
	SELECT c.customer_id, p.product_key
	FROM customer c 
	JOIN product p ON c.product_key = p.product_key
)
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM product)
ORDER BY 1;

-- Solution without checking

SELECT customer_id
FROM customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM product)
ORDER BY 1;