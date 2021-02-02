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
    CHECK(price > CAST(0 AS MONEY))
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

CREATE TABLE book_author(
    book_id BIGINT NOT NULL,
    author_id BIGINT NOT NULL,
    FOREIGN KEY(book_id) REFERENCES book(id),
    FOREIGN KEY(author_id) REFERENCES author(id),
    UNIQUE(book_id, author_id)
);

CREATE TABLE genre(
    id BIGSERIAL NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(name)
);

CREATE TABLE book_genre(
    book_id BIGINT NOT NULL,
    genre_id BIGINT NOT NULL,
    FOREIGN KEY(book_id) REFERENCES book(id),
    FOREIGN KEY(genre_id) REFERENCES genre(id),
    UNIQUE(book_id, genre_id)
);

INSERT INTO book(title, year, isbn, price) VALUES
    ('Алгоритмы: построение и анализ', '1990-01-01', '978-5-8459-2016-4', 5500),
    ('Война и мир', '1865-01-01', '978-5-389-07123-0', 297),
    ('Евгений Онегин', '1825-01-01', '978-5-17-093121-7', 190),
    ('Курс дифференциального и интегрального исчисления', '1947-01-01',
        '978-5-8114-7061-7', 2995),
    ('Преступление и наказание', '1866-01-01', '978-5-17-090630-7', 176);

INSERT INTO author(full_name, birth_date, death_date) VALUES
    ('Александр Сергеевич Пушкин', '1799-06-06', '1837-02-10'),
    ('Григорий Михайлович Фихтенгольц', '1888-06-05', '1959-06-26'),
    ('Лев Николаевич Толстой', '1828-09-09', '1910-11-20'),
    ('Фёдор Михайлович Достоевский', '1821-11-11', '1881-02-09');
INSERT INTO author(full_name, birth_date) VALUES
    ('Клиффорд Штайн', '1965-12-14'),
    ('Рональд Линн Ривест', '1947-01-01'),
    ('Томас Х. Кормен', '1956-01-01'),
    ('Чарльз Эрик Лейзерсон', '1953-11-10');

INSERT INTO genre(name) VALUES
    ('Компьютерные науки'),
    ('Математика'),
    ('Роман');
