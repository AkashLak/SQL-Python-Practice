WITH ranked_spending AS (
  SELECT category, product, SUM(spend) AS total_spend,
         RANK() OVER (PARTITION BY category 
                ORDER BY SUM(spend) DESC) AS ranking
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY product, category
  )
  
SELECT category, product, total_spend
FROM ranked_spending
WHERE ranking <= 2
ORDER BY category
