-- Select the genre and the count of shows linked to that genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres  -- From the tv_genres table
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  -- Join with tv_show_genres
GROUP BY tv_genres.name  -- Group by genre name
HAVING COUNT(tv_show_genres.show_id) > 0  -- Only include genres with linked shows
ORDER BY number_of_shows DESC;  -- Sort by the number of shows in descending order
