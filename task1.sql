CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author_id INT,
    publication_year INT,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books (id)
);

INSERT INTO authors (first_name, last_name)
VALUES ('Alex', 'Borisevich'),
       ('John', 'Doe'),
       ('Jane', 'Smith'),
       ('Michael', 'Johnson');

INSERT INTO books (title, author_id, publication_year)
VALUES ('Book 1', 1, 2020),
       ('Book 2', 2, 2018),
       ('Book 3', 1, 2018),
       ('Book 4', 2, 2018),
       ('Book 5', 2, 2018),
       ('Book 6', NULL, 2018),
       ('Book 7', 3, 2021),
       ('Book 8', 3, 2021);

INSERT INTO sales (book_id, quantity)
VALUES (1, 10),
       (1, 7),
       (2, 5),
       (3, 14),
       (3, 2),
       (4, 8),
       (5, 7),
       (8,12),
       (6, 9);