-- ============================================================================
-- Sample Data (Optional)
-- ============================================================================

-- Insert sample users
INSERT INTO Users (first_name, last_name, date_of_birth) VALUES
    ('John', 'Doe', '1990-05-15'),
    ('Jane', 'Smith', '1985-08-22'),
    ('Mike', 'Johnson', '1992-12-03');

-- Insert sample songs
INSERT INTO Songs (song_title, artist, genre) VALUES
    ('Bohemian Rhapsody', 'Queen', 'Rock'),
    ('Shape of You', 'Ed Sheeran', 'Pop'),
    ('Hotel California', 'Eagles', 'Rock'),
    ('Billie Jean', 'Michael Jackson', 'Pop'),
    ('Stairway to Heaven', 'Led Zeppelin', 'Rock');

-- Insert sample user-song relationships
INSERT INTO User_Songs (User_ID, Song_ID) VALUES
    (1, 1), -- John likes Bohemian Rhapsody
    (1, 3), -- John likes Hotel California
    (1, 5), -- John likes Stairway to Heaven
    (2, 2), -- Jane likes Shape of You
    (2, 4), -- Jane likes Billie Jean
    (3, 1), -- Mike likes Bohemian Rhapsody
    (3, 2), -- Mike likes Shape of You
    (3, 3); -- Mike likes Hotel California
-- ============================================================================
