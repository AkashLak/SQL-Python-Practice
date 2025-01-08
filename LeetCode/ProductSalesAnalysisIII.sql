WITH smallest_year AS (
   SELECT product_id, MIN(year) AS first_year
   FROM Sales
   GROUP BY product_id
)


SELECT s.product_id, first_year, quantity, price
FROM Sales s
JOIN smallest_year sy
ON s.product_id = sy.product_id AND s.year = sy.first_year

