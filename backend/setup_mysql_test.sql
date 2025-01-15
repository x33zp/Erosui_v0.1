-- Creates a database 'ersu_test_db', a new user 'ersu_test' that has all priviledges on the database.
-- and select priviledges on the database 'performance_schema'

CREATE DATABASE IF NOT EXISTS ersu_test_db;
CREATE USER IF NOT EXISTS 'ersu_test'@'localhost' IDENTIFIED BY '081016Xx$';
GRANT ALL PRIVILEGES ON ersu_test_db.* TO 'ersu_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'ersu_test'@'localhost';
