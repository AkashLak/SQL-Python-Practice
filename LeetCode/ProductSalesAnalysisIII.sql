WITH smallest_year AS (
   SELECT product_id, MIN(year) AS first_year
   FROM Sales
   GROUP BY product_id
)
