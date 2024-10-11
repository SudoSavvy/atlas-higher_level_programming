-- Select the titles of all Comedy shows
SELECT tv_shows.title
FROM tv_shows  -- Start from the tv_shows table
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Join with tv_show_genres on show ID
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id  -- Join with tv_genres on genre ID
WHERE tv_genres.name = 'Comedy'  -- Filter for the genre "Comedy"
ORDER BY tv_shows.title ASC;  -- Sort by show title in ascending order
