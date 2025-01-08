WITH supercloud_customer AS (
  SELECT cc.customer_id, COUNT(DISTINCT p.product_category) AS product_count
  FROM customer_contracts cc
  JOIN products p 
  ON cc.product_id = p.product_id
  GROUP BY cc.customer_id
  )
  
SELECT customer_id
FROM supercloud_customer
WHERE product_count = (
SELECT COUNT(DISTINCT product_category) 
FROM products
)
