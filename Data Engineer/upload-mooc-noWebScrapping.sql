-- Create the database if it doesn't exist
DROP DATABASE IF EXISTS mooc;
CREATE DATABASE IF NOT EXISTS mooc;
USE mooc;

-- Create the table
DROP TABLE IF EXISTS mooc;
CREATE TABLE IF NOT EXISTS mooc (
    title VARCHAR(255),
    institution VARCHAR(255),
    url VARCHAR(255),
    id VARCHAR(255),
    mooc VARCHAR(255),
    summary TEXT,
    n_subscribers VARCHAR(255),
    modality VARCHAR(255),
    instructors VARCHAR(255),
    level VARCHAR(255),
    subject VARCHAR(255),
    language VARCHAR(255),
    subtitles VARCHAR(255),
    effort VARCHAR(255),
    duration VARCHAR(255),
    price VARCHAR(255),
    description TEXT,
    curriculum TEXT,
    paid VARCHAR(255),
    n_reviews VARCHAR(255),
    n_lectures VARCHAR(255),
    published VARCHAR(255)
);

-- Load the data from CSV file
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/mooc-noWebScrapping.csv'
INTO TABLE mooc
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;