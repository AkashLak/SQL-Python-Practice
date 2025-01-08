WITH first_login AS (
   SELECT player_id, MIN(event_date) AS first_login_date
   FROM Activity
   GROUP BY player_id
)


SELECT ROUND((COUNT(DISTINCT a1.player_id) /
      (SELECT COUNT(DISTINCT player_id)
      FROM Activity)), 2) AS fraction
FROM first_login fl
JOIN Activity a1
ON a1.event_date = DATE_ADD(first_login_date, INTERVAL 1 DAY)
AND a1.player_id = fl.player_id
