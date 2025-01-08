SELECT p.product_id, ROUND(COALESCE(SUM(p.price * units),0) / COALESCE(SUM(units), 1), 2) AS average_price
FROM Prices p 
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND u.purchase_date BETWEEN start_date AND end_date
GROUP BY p.product_id
