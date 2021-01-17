DROP DATABASE IF EXISTS book_store_database;
DROP USER IF EXISTS book_store_user;

--Just for examples. Don't save password in git.
CREATE USER book_store_user PASSWORD 'IX#xZ&5kojzu!*hQyVRo';
CREATE DATABASE book_store_database WITH
    OWNER book_store_user
    ENCODING 'UTF8';

CREATE TABLE book(
    id BIGSERIAL NOT NULL,
    title VARCHAR(255) NOT NULL,
    year DATE NOT NULL,
    isbn CHAR(13) NOT NULL,
    price l NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(isbn),
);

CREATE TABLE author(
    id BIGSERIAL NOT NULL,
    name BIGSERIAL NOT NULL,
    birthdate DATE NOT NULL,
    deathdate DATE DEFAULT '9999-31-12',
    PRIMARY KEY(id),
    UNIQUE(name, birthdate)
);

CREATE TABLE written_by(
    book_id BIGINT NOT NULL,
    author_id BIGINT NOT NULL,
    UNIQUE(book_id, author_id)
);

CREATE TABLE genre(
    id BIGSERIAL NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(name),
);

CREATE TABLE belongs_to(
    book_id BIGINT NOT NULL,
    genre_id BIGINT NOT NULL,
    UNIQUE(book_id, genre_id)
);
