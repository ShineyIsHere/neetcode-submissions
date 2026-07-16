-- Write your query below
select distinct sales_person.name from sales_person
LEFT JOIN orders
ON orders.sales_id = sales_person.sales_id
WHERE sales_person.sales_id NOT IN (SELECT distinct orders.sales_id FROM orders 
                                    JOIN company 
                                    ON orders.com_id = company.com_id 
                                    WHERE company.name = 'CRIMSON')