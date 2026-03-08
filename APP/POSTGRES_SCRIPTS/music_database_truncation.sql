-- ============================================================================
-- Music Database Schema
-- Truncate tables for Users, Songs, and User-Song relationships
-- Expeditious testing
-- ============================================================================
TRUNCATE TABLE IF EXISTS User_Songs CASCADE;
TRUNCATE TABLE IF EXISTS Songs CASCADE;
TRUNCATE TABLE IF EXISTS Users CASCADE
