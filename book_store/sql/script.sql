DROP DATABASE IF EXISTS book_store_database;
DROP USER IF EXISTS book_store_user;

CREATE USER book_store_user PASSWORD 'IX#xZ&5kojzu!*hQyVRo';
CREATE DATABASE book_store_database WITH
    OWNER book_store_user
    ENCODING 'UTF8';
