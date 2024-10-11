-- Select the title of the TV shows and their corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows  -- From the tv_shows table
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id  -- Join with the tv_show_genres table on matching IDs
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;  -- Sort the results by show title and genre ID in ascending order
