-- Select the titles of all shows and their corresponding genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows  -- Start from the tv_shows table
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Left join with tv_show_genres on show ID
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id  -- Left join with tv_genres on genre ID
ORDER BY tv_shows.title ASC, tv_genres.name ASC;  -- Sort by show title and genre name in ascending order
