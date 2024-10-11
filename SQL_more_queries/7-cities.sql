-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the cities table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,   -- id is unique, auto-generated, not null
    state_id INT NOT NULL,                   -- state_id can't be null, foreign key
    name VARCHAR(256) NOT NULL,              -- name can't be null
    PRIMARY KEY (id),                        -- id is the primary key
    FOREIGN KEY (state_id) REFERENCES states(id)  -- foreign key referencing the id of states table
);
