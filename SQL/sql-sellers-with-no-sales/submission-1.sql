-- Write your query below
SELECT seller.seller_name FROM seller
WHERE seller.seller_id  <> all(select distinct seller_id from orders WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31' )
ORDER BY seller.seller_name