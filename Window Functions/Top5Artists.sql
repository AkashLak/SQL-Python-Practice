WITH top_10_rank AS (
  SELECT a.artist_name,
         DENSE_RANK() OVER (ORDER BY COUNT(s.song_id) DESC) AS artist_rank
  FROM artists a
  JOIN songs s
  ON a.artist_id = s.artist_id
  JOIN global_song_rank gsr
  ON s.song_id = gsr.song_id
  WHERE gsr.rank <= 10
  GROUP BY a.artist_name
)

SELECT artist_name, artist_rank
FROM top_10_rank
WHERE artist_rank <= 5
