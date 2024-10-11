-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,  -- id must be unique and has a default value of 1
    name VARCHAR(256)
);
