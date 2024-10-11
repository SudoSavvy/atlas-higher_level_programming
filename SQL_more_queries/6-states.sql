-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,  -- id is unique, auto-generated, not null
    name VARCHAR(256) NOT NULL,  -- name can't be null
    PRIMARY KEY (id)  -- id is the primary key
);
