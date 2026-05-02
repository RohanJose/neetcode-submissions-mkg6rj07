-- Write your query below
SELECT c.customer_id,c.customer_name FROM customers c
JOIN orders o on c.customer_id=o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING
 SUM(CASE WHEN o.product_name = 'A' Then 1 else 0 END ) > 0
 AND SUM(CASE WHEN o.product_name='B' Then 1 else 0 END ) > 0
 AND SUM(CASE WHEN o.product_name = 'C' Then 1 else 0 END) = 0
ORDER BY c.customer_name
;
