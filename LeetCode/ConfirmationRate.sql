SELECT s.user_id, COALESCE(ROUND(COUNT(CASE WHEN action = 'confirmed' THEN 1 END)
      / COUNT(CASE WHEN action IN ('confirmed', 'timeout') THEN 1 END), 2),0) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id
