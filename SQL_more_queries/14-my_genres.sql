-- Select the genre names for the show "Dexter"
SELECT tv_genres.name
FROM tv_genres  -- Select from the tv_genres table
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  -- Join with tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id  -- Join with tv_shows
WHERE tv_shows.title = 'Dexter'  -- Filter for the show "Dexter"
ORDER BY tv_genres.name ASC;  -- Sort by genre name in ascending order
