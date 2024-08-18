DROP TABLE IF EXISTS actors;
CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('Leonardo', 'DiCaprio', '1974-11-11', 1),
('Tom', 'Hanks', '1956-07-09', 2),
('Denzel', 'Washington', '1954-12-28', 2);
SELECT COUNT(*) AS actor_count FROM actors;
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES (' ', 'Gaga', ' ', ' ');
