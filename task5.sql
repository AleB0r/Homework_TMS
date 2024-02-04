-- Найдите автора с наибольшим количеством проданных книг, используя подзапросы и JOIN
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.first_name, authors.last_name
HAVING SUM(sales.quantity) = (
    SELECT MAX(total_sales)
    FROM (
        SELECT SUM(sales.quantity) AS total_sales
        FROM authors
        INNER JOIN books ON authors.id = books.author_id
        INNER JOIN sales ON books.id = sales.book_id
        GROUP BY authors.first_name, authors.last_name
    ) AS subquery
);

-- Найдите книги, которые были проданы в количестве, превышающем среднее количество продаж всех книг, используя подзапросы и JOIN
SELECT books.title, sales.quantity
FROM books
INNER JOIN sales ON books.id = sales.book_id
WHERE sales.quantity > (
    SELECT AVG(quantity)
    FROM sales
);

--Найдите книги, которые были проданы в количестве, превышающем среднее количество продаж каждой из книг, используя подзапросы и JOIN
SELECT b.title, s.quantity
FROM books b
JOIN sales s ON b.id = s.book_id
WHERE s.quantity > (
    SELECT MAX(average_sales)
    FROM (
        SELECT AVG(quantity) AS average_sales
        FROM sales
        GROUP BY book_id
    ) AS subquery
);