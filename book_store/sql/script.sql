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
    price MONEY NOT NULL,
    PRIMARY KEY(id),
    -- title is not UNIQUE
    UNIQUE(isbn),
    CHECK(year = DATE_TRUNC('year', year) AND year < current_date),
    CHECK(isbn SIMILAR TO '\d{13}'),
    CHECK(price > 0)
);

CREATE TABLE author(
    id BIGSERIAL NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    death_date DATE NOT NULL DEFAULT '9999-12-31',
    PRIMARY KEY(id),
    -- full_name is not UNIQUE
    UNIQUE(full_name, birth_date)
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
    UNIQUE(name)
);

CREATE TABLE belongs_to(
    book_id BIGINT NOT NULL,
    genre_id BIGINT NOT NULL,
    UNIQUE(book_id, genre_id)
);
