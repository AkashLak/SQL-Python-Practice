WITH organized_order AS (
   SELECT customer_id, order_date, customer_pref_delivery_date
   FROM (
       SELECT customer_id, order_date, customer_pref_delivery_date, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS rn
       FROM delivery
   )
   where rn = 1
)
SELECT ROUND(COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END) /
      COUNT(*) * 100, 2) AS immediate_percentage
FROM organized_order
