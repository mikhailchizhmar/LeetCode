-- https://leetcode.com/problems/immediate-food-delivery-ii

WITH cte AS (
	SELECT *, FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_date
	FROM delivery
)

SELECT ROUND(
	COUNT(*) FILTER (WHERE order_date = customer_pref_delivery_date) * 100.0 / COUNT(*), 2
) AS immediate_percentage
FROM cte
WHERE order_date = first_date;

-- Solution without window functions

SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1
                ELSE 0 END)*100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
                SELECT customer_id,
                    MIN(order_date)
                    FROM Delivery
                    GROUP BY customer_id
);