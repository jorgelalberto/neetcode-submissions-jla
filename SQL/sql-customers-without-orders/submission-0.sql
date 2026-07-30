-- Write your query below
SELECT name FROM customers
LEFT JOIN orders
ON orders.customer_id = customers.id
WHERE customer_id IS NULL;