-- ============================================================================
-- Useful Queries (Examples)
-- ============================================================================

-- Get all unique users, in alphabetical order
SELECT DISTINCT first_name, last_name
FROM Users u
ORDER BY u.first_name ASC, u.last_name ASC;

-- Insert a new user
INSERT INTO Users (first_name, last_name, email, `password`)
VALUES










-- -- Get all songs for a specific user
-- SELECT s.song_title, s.artist, s.genre 
-- FROM Users u
-- JOIN User_Songs us ON u.User_Id = us.User_ID
-- JOIN Songs s ON us.Song_ID = s.Song_ID
-- WHERE u.User_Id = 1;

-- -- Get all users who like a specific song
-- SELECT u.first_name, u.last_name
-- FROM Users u
-- JOIN User_Songs us ON u.User_Id = us.User_ID
-- JOIN Songs s ON us.Song_ID = s.Song_ID
-- WHERE s.song_title = 'Bohemian Rhapsody';

-- -- Count songs per user
-- SELECT u.first_name, u.last_name, COUNT(us.Song_ID) as song_count
-- FROM Users u
-- LEFT JOIN User_Songs us ON u.User_Id = us.User_ID
-- GROUP BY u.User_Id, u.first_name, u.last_name
-- ORDER BY song_count DESC;

-- -- ============================================================================
