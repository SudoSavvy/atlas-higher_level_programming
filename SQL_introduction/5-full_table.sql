-- This script prints the full description of the first_table
SELECT 
    TABLE_NAME AS 'Table',
    CREATE_STATEMENT AS 'Create Table'
FROM 
    information_schema.TABLES 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' 
    AND TABLE_NAME = 'first_table';
