SELECT g.genre_name, t.track_name, a.artist_name, t.popularity, f.danceability, f.energy
FROM tracks AS t
JOIN genres AS g ON t.genre_id = g.genre_id
JOIN artists AS a ON t.artist_id = a.artist_id
JOIN features AS f ON t.track_id = f.track_id
WHERE g.genre_name = 'pop'
