WITH highest_num AS(
   SELECT num
   FROM MyNumbers
   GROUP BY num
   HAVING COUNT(num) = 1
   ORDER BY num DESC
   LIMIT 1
)
SELECT (CASE WHEN COUNT(num) = 0 THEN NULL ELSE num END) AS num
FROM highest_num
