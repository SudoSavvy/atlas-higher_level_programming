-- This script prints the full description of the first_table
SELECT 
    TABLE_NAME AS 'Table',
    CONCAT(
        'CREATE TABLE `', TABLE_NAME, '` (',
        '`id` INT NOT NULL AUTO_INCREMENT,',
        '`name` VARCHAR(128) DEFAULT NULL,',
        '`c` CHAR(1) DEFAULT NULL,',
        '`created_at` DATE DEFAULT NULL,',
        'PRIMARY KEY (`id`)',
        ') ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
    ) AS 'Create Table'
FROM 
    information_schema.TABLES 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' 
    AND TABLE_NAME = 'first_table';
