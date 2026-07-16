-- Write your query below
SELECT customers.name FROM customers 
WHERE customers.id <> ALL ( SELECT customer_id FROM orders);