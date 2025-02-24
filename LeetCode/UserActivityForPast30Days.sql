WITH certain_date AS (
   SELECT user_id, activity_date
   FROM Activity
   WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
)


SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM certain_date
GROUP BY activity_date
