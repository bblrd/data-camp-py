# Intro to SQL for Data Science on DataCamp

#######################################

# Part 1: Selecting columns

#######################################

## Onboarding | Errors
SELECT 'DataCamp <3 SQL'
AS result;

## Onboarding | Bullet Exercises
SELECT 'SQL is cool!'
AS result;

## SELECTing single columns
SELECT name
FROM people;

## SELECTing multiple columns
SELECT *
FROM films;

## SELECT DISTINCT
SELECT DISTINCT role
FROM roles;

## Learning to COUNT
SELECT COUNT(*)
FROM reviews;

## Practice with COUNT
SELECT COUNT(DISTINCT country)
FROM films;

#######################################

# Part 2: Filtering rows

#######################################

## Simple filtering of numeric values

# Get all details for all films released in 2016.
SELECT *
FROM films
WHERE release_year = 2016;

# Get the number of films released before 2000.
SELECT COUNT(title)
FROM films
WHERE release_year < 2000;

# Get the title and release year of films released after 2000.
SELECT title, release_year
FROM films
WHERE release_year > 2000;

## Simple filtering of text

# Get all details for all French language films.
SELECT *
FROM films
WHERE language = 'French';

# Get the name and birth date of the person born on November 11th, 1974.
# Remember to use ISO date format ('1974-11-11')!
SELECT name
FROM people
WHERE birthdate = '1974-11-11';

# Get the number of Hindi language films.
SELECT COUNT(*)
FROM films
WHERE language = 'Hindi';

# Get all details for all films with an R certification.
SELECT *
FROM films
WHERE certification = 'R';

## WHERE AND

# Get the title and release year for all Spanish language films released before 2000.
Select title, release_year
from films
where language = 'Spanish' and release_year < 2000;

# Get all details for Spanish language films released after 2000.
Select *
from films
where language = 'Spanish' and release_year > 2000;

# Get all details for Spanish language films released after 2000, but before 2010.
Select *
from films
where language = 'Spanish' and release_year > 2000 and release_year < 2010;

## WHERE AND OR (2)

# Get the title and release year for films released in the 90s.
# Now, build on your query to filter the records to only include French or Spanish language films.
# Finally, restrict the query to only return films that took in more than $2M gross.
select title, release_year
from films
where (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish')
AND gross > 2000000;

## BETWEEN (2)

# Get the title and release year of all films released between 1990 and 2000 (inclusive).
# Now, build on your previous query to select only films that have budgets over $100 million.
# Now restrict the query to only return Spanish language films.
# Finally, modify to your previous query to include all Spanish language or French language
# films with the same criteria as before. Don't forget your parentheses!
select title, release_year
from films
where release_year >= 1990 and release_year <= 2000
and budget > 100000000
and (language = 'Spanish' or language = 'French');

## WHERE IN

# Get the title and release year of all films released in 1990 or 2000 that were longer
# than two hours. Remember, duration is in minutes!
select title, release_year
from films
where release_year IN (1990, 2000)
and duration > 120;

#Get the title and language of all films which were in English, Spanish, or French.
select title, language
from films
where language IN ('English', 'Spanish', 'French');

# Get the title and certification of all films with an NC-17 or R certification.
select title, certification
from films
where certification IN ('NC-17', 'R');

## NULL and IS NULL

# Get the names of people who are still alive, i.e. whose death date is missing.
select name
from people
where deathdate IS NULL;

# Get the title of every film which doesn't have a budget associated with it.
select title
from films
where budget IS NULL;

# Get the number of films which don't have a language associated with them.
select COUNT(title)
from films
where language IS NULL;

## LIKE and NOT LIKE

# Get the names of all people whose names begin with 'B'. The pattern you need is 'B%'.
select name
from people
where name LIKE 'B%';

# Get the names of people whose names have 'r' as the second letter. The pattern you need is '_r%'.
select name
from people
where name LIKE '_r%';

# Get the names of people whose names don't start with A. The pattern you need is 'A%'.
select name
from people
where name NOT LIKE 'A%';

#######################################

# Part 3: Aggregate Functions

#######################################

## Aggregate functions

# Use the SUM function to get the total duration of all films.
select SUM(duration)
from films;

# Get the average duration of all films.
select AVG(duration)
from films;

# Get the duration of the shortest film.
select MIN(duration)
from films;

# Get the duration of the longest film.
select MAX(duration)
from films;

## Aggregate functions practice

# Use the SUM function to get the total amount grossed by all films.
select sum(gross)
from films;

# Get the average amount grossed by all films.
select avg(gross)
from films;

# Get the amount grossed by the worst performing film.
select min(gross)
from films;

# Get the amount grossed by the best performing film.
select max(gross)
from films;

## Combining aggregate functions with WHERE

# Use the SUM function to get the total amount grossed by all films made in the year 2000 or later.
select sum(gross)
from films
where release_year >= 2000;

# Get the average amount grossed by all films whose titles start with the letter 'A'.
select avg(gross)
from films
where title LIKE 'A%';

# Get the amount grossed by the worst performing film in 1994.
select min(gross)
from films
where release_year = '1994';

# Get the amount grossed by the best performing film between 2000 and 2012, inclusive.
select max(gross)
from films
where release_year >= 2000 and release_year <= 2012;

## It's AS simple AS aliasing

# Get the title and net profit (the amount a film grossed, minus its budget) for all films. Alias the net profit as net_profit.
select title, (gross - budget) AS net_profit
from films;

# Get the title and duration in hours for all films. The duration is in minutes, so you'll need to divide by 60.0
# to get the duration in hours. Alias the duration in hours as duration_hours.
select title, (duration / 60.0) AS duration_hours
from films;

# Get the average duration in hours for all films, aliased as avg_duration_hours.
select avg(duration) / 60.0 AS avg_duration_hours
from films;

## Even more aliasing

# Get the percentage of people who are no longer alive. Alias the result as percentage_dead. Remember to use 100.0 and not 100!
select (Count(deathdate) * 100.0 / Count(*)) AS percentage_dead
from people;

# Get the number of years between the newest film and oldest film. Alias the result as difference.
select max(release_year) - min(release_year) AS difference
from films;

# Get the number of decades the films table covers. Alias the result as number_of_decades.
# The top half of your fraction should be enclosed in parentheses.
select (max(release_year) - min(release_year)) / 10.0  AS number_of_decades
from films;

#######################################

# Part 4: Sorting, grouping and joins

#######################################

## Sorting single columns

# Get the names of people from the people table, sorted alphabetically.
select name
from people
order by name;

# Get the names of people, sorted by birth date.
select name
from people
order by birthdate;

# Get the birth date and name for every person, in order of when they were born.
select name, birthdate
from people
order by birthdate;

## Sorting single columns (2)

# Get the title of films released in 2000 or 2012, in the order they were released.
select title
from films
where release_year IN (2000, 2012)
order by release_year;

# Get all details for all films except those released in 2015 and order them by duration.
select *
from films
where release_year NOT IN (2015)
order by duration;

# Get the title and gross earnings for movies which begin with the letter 'M' and order the results alphabetically.
select *
from films
where release_year NOT IN (2015)
order by duration;

## Sorting single columns (DESC)

# Get the IMDB score and film ID for every film from the reviews table, sorted from highest to lowest score.
select imdb_score, film_id
from reviews
order by imdb_score desc;

# Get the title for every film, in reverse order.
select title
from films
order by title desc;

# Get the title and duration for every film, in order of longest duration to shortest.
select title, duration
from films
order by duration desc;

## Sorting multiple columns

# Get the birth date and name of people in the people table, in order of when they were born and alphabetically by name.
select birthdate, name
from people
order by birthdate, name;

# Get the release year, duration, and title of films ordered by their release year and duration.
select release_year, duration, title
from films
order by release_year, duration;

# Get certifications, release years, and titles of films ordered by certification (alphabetically) and release year.
select certification, release_year, title
from films
order by certification, release_year;

# Get the names and birthdates of people ordered by name and birth date.
select name, birthdate
from people
order by name, birthdate;

## GROUP BY practice

# Get the release year and count of films released in each year.
select release_year, COUNT(title)
from films
group by release_year;

# Get the release year and average duration of all films, grouped by release year.
select release_year, avg(duration)
from films
group by release_year;

# Get the release year and largest budget for all films, grouped by release year.
select release_year, max(budget)
from films
group by release_year;

# Get the IMDB score and count of film reviews grouped by IMDB score in the reviews table.
select imdb_score, count(*)
from reviews
group by imdb_score;

## GROUP BY practice (2)

# Get the release year and lowest gross earnings per release year.
select release_year, min(gross)
from films
group by release_year;

# Get the language and total gross amount films in each language made.
select language, sum(gross)
from films
group by language;

# Get the country and total budget spent making movies in each country.
select country, sum(budget)
from films
group by country;

# Get the release year, country, and highest budget spent making a film for each year,
# for each country. Sort your results by release year and country.
select release_year, country, max(budget)
from films
group by release_year, country
order by release_year, country;

# Get the country, release year, and lowest amount grossed per release year per country. Order your results by country and release year.
select country, release_year, min(gross)
from films
group by country, release_year
order by country, release_year;

## HAVING a great time

# In how many different years were more than 200 movies released?
SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 200;

## All together now

# Get the release year, budget and gross earnings for each film in the films table.
select release_year, budget, gross
from films;

# Modify your query so that only records with a release_year after 1990 are included.
select release_year, budget, gross
from films
where release_year > 1990;

# Remove the budget and gross columns, and group your results by release year.
select release_year
from films
where release_year > 1990
group by release_year;

# Modify your query to include the average budget and average gross earnings for the results you
# have so far. Alias the average budget as avg_budget; alias the average gross earnings as avg_gross.
select release_year, avg(budget) AS avg_budget, avg(gross) AS avg_gross
from films
where release_year > 1990
group by release_year;

# Modify your query so that only years with an average budget of greater than $60 million are included.
select release_year, avg(budget) AS avg_budget, avg(gross) AS avg_gross
from films
where release_year > 1900
group by release_year
having avg(budget) > 60000000;

# Finally, modify your query to order the results from highest average gross earnings to lowest.
select release_year, avg(budget) AS avg_budget, avg(gross) AS avg_gross
from films
where release_year > 1900
group by release_year
having avg(budget) > 60000000
order by avg_gross desc;

## All together now (2)

# select country, average budget, average gross
select country, avg(budget) as avg_budget, avg(gross) as avg_gross
# from the films table
from films
# group by country
group by country
# where the country has more than 10 titles
having count(title) > 10
# order by country
order by country
# limit to only show 5 results
limit 5;

## A taste of things to come

# Submit the code in the editor and inspect the results.
SELECT title, imdb_score
FROM films
JOIN reviews
ON films.id = reviews.film_id
WHERE title = 'To Kill a Mockingbird';
