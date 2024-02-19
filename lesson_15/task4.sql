SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.first_name, authors.last_name;

SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id
GROUP BY authors.first_name, authors.last_name;