SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;

SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id
ORDER BY last_name,first_name;

SELECT books.title, authors.first_name, authors.last_name
FROM authors
RIGHT JOIN books ON books.author_id = authors.id;