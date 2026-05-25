-- Write your query below
SELECT customers.name
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
GROUP BY customers.name
HAVING COUNT(orders.id) = 0