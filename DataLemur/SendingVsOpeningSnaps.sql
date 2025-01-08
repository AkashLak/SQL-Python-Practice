SELECT age_bucket, 
        ROUND(100 * (SUM(a.time_spent) FILTER (WHERE activity_type = 'send') / SUM(a.time_spent)), 2) AS send_perc,
        ROUND(100 * (SUM(a.time_spent) FILTER (WHERE activity_type = 'open') / SUM(a.time_spent)),2) AS open_perc
FROM activities a
JOIN age_breakdown ab
ON a.user_id = ab.user_id
WHERE activity_type IN ('open', 'send')
GROUP BY age_bucket
