WITH FriendCount AS (
SELECT requester_id AS id, COUNT(DISTINCT accepter_id) AS num
FROM RequestAccepted
GROUP BY requester_id
UNION ALL
SELECT accepter_id AS id, COUNT(DISTINCT requester_id) AS num
FROM RequestAccepted
GROUP BY accepter_id
),
Total_Count AS (
    SELECT id, SUM(num) AS total_friends
    FROM FriendCount
    GROUP BY id
)
SELECT id, total_friends as num
FROM Total_Count
ORDER BY num DESC
LIMIT 1
