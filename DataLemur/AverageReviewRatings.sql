SELECT EXTRACT(MONTH FROM submit_date) AS mnth, product_id AS product, ROUND(AVG(stars),2) AS avg_stars
FROM reviews
GROUP BY EXTRACT(MONTH FROM submit_date), product_id
ORDER BY mnth, product_id
