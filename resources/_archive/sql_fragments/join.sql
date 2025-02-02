
-- INNER JOIN ( OLD FORMAT)
SELECT * 
FROM cutomer, orders
WHERE customer_id = cust_id;


-- INNER JOIN ( READABLE AND MODERN FORMAT)
SELECT *
FROM cutomer INNER JOIN orders
ON customer_id = cust_id;