--SELECT * FROM language;
--SELECT f.title, f.description, l.name AS language_name
--FROM film f
--JOIN language l ON f.language_id = l.language_id;

--SELECT f.title, f.description, l.name AS language_name
--FROM language l
--LEFT JOIN film f ON l.language_id = f.language_id;

--CREATE TABLE new_film (
--id SERIAL PRIMARY KEY,
--name VARCHAR(255) NOT NULL
--);

--INSERT INTO new_film (name) VALUES
--('The lord of the rings'),
--('Knigt'),
--('Nightmare'),
--('Hobbit');
--CREATE TABLE customer_review (
--review_id SERIAL PRIMARY KEY,
--film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
--language_id INT REFERENCES language(language_id),
--title VARCHAR(255) NOT NULL,
--rating INT CHECK (rating BETWEEN 1 AND 10),
--review_text TEXT,
--last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
--);

--INSERT INTO customer_review (film_id, language_id, title, rating, review_text)
--VALUES
--(1, 1, 'Amazing Movie', 9, 'An outstanding film with great visuals.'),
--(2, 2, 'Disappointing', 4, 'The story was lacking, and the execution was poor.');

SELECT language_id, name FROM language;
UPDATE film
SET language_id = 3
WHERE film_id = 1;

UPDATE film
SET language_id = 4
WHERE language_id = 1;

--DROP TABLE customer_review;

SELECT COUNT(*)AS unreturned_items_count
FROM rental
WHERE return_date IS NULL;

SELECT f.title, f.rental_rate
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
GROUP BY f.film_id, f.title, f.rental_rate
ORDER BY f.rental_rate DESC
LIMIT 30;

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
AND f.description LIKE '%sumo wrestler%';

SELECT title
FROM film
WHERE rating = 'R'
AND length > 1;

--SELECT f.title
--FROM film f
--JOIN rental r ON f.film_id = r.film_id
--JOIN payment p ON r.rental_id = p.rental_id
--JOIN customer c ON r.customer_id = c.customer_id
--WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
--AND p.amount > 4.00
--AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';


SELECT f.title
FROM film f
JOIN rental r ON f.film_id = r.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title LIKE '%boat%' OR f.description LIKE '%boat%')
ORDER BY f.rental_rate DESC;







