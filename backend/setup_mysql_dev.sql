-- Creates a database 'ersu_dev_db', a new user 'ersu_dev' that has all priviledges on the database.
-- and select priviledges on the database 'performance_schema'

CREATE DATABASE IF NOT EXISTS ersu_dev_db;
CREATE USER IF NOT EXISTS 'ersu_dev'@'localhost' IDENTIFIED BY '081016Xx$';
GRANT ALL PRIVILEGES ON ersu_dev_db.* TO 'ersu_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'ersu_dev'@'localhost';
