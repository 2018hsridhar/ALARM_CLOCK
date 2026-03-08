-- ============================================================================
-- Music Database Schema
-- Creates tables for Users, Songs, and User-Song relationships
-- ============================================================================

-- Drop tables if they exist (in reverse dependency order)
DROP TABLE IF EXISTS User_Songs CASCADE;
DROP TABLE IF EXISTS Songs CASCADE;
DROP TABLE IF EXISTS Users CASCADE;

-- ============================================================================
-- Table 1: Users
-- Stores user information
-- ============================================================================
CREATE TABLE Users (
    User_Id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- Optional: Add constraints
    CONSTRAINT chk_birth_date CHECK (date_of_birth <= CURRENT_DATE),
    CONSTRAINT chk_first_name_length CHECK (LENGTH(first_name) >= 1),
    CONSTRAINT chk_last_name_length CHECK (LENGTH(last_name) >= 1)
);

-- ============================================================================
-- Table 2: Songs
-- Stores song information
-- ============================================================================
CREATE TABLE Songs (
    Song_ID SERIAL PRIMARY KEY,
    song_title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,    
    
    -- Optional: Add constraints
    CONSTRAINT chk_song_title_length CHECK (LENGTH(song_title) >= 1),
    CONSTRAINT chk_artist_length CHECK (LENGTH(artist) >= 1),
    CONSTRAINT chk_genre_length CHECK (LENGTH(genre) >= 1)
);

-- ============================================================================
-- Table 3: User_Songs (Junction Table)
-- Stores the many-to-many relationship between Users and Songs
-- Note: 1:n cardinality means one user can have many songs
-- ============================================================================
CREATE TABLE User_Songs (
    Record_Id SERIAL PRIMARY KEY,
    User_ID INTEGER NOT NULL,
    Song_ID INTEGER NOT NULL,
    
    -- Foreign key constraints
    -- Prevent orphaned records in User_Songs
    -- and ensure referential integrity
    -- with automatic cascading on delete/update
    CONSTRAINT fk_user_songs_user_id 
        FOREIGN KEY (User_ID) REFERENCES Users(User_Id) 
        ON DELETE CASCADE ON UPDATE CASCADE,
        
    CONSTRAINT fk_user_songs_song_id 
        FOREIGN KEY (Song_ID) REFERENCES Songs(Song_ID) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    
    -- Optional: Prevent duplicate user-song combinations
    CONSTRAINT uq_user_song UNIQUE (User_ID, Song_ID),
    
    -- Optional: Add timestamp for when the relationship was created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- ============================================================================
-- Sample Data (Optional)
-- Single initialization script
-- This section inserts sample data into the Users, Songs, and User_Songs tables
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
