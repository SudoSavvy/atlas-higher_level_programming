-- Select the title of TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows  -- From the tv_shows table
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Update with the correct column name
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;  -- Sort the results
