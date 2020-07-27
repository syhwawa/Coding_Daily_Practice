## More Join

#### Busy years for Rock Hudson
11.
Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
```
SELECT yr,COUNT(title) FROM
  movie JOIN casting ON movie.id=movieid
        JOIN actor   ON actorid=actor.id
WHERE name='Rock Hudson'
GROUP BY yr
HAVING COUNT(title) > 1
```
####Lead actor in Julie Andrews movies
12.
List the film title and the leading actor for all of the films 'Julie Andrews' played in.

Did you get "Little Miss Marker twice"?
```
select title, name from
  movie JOIN casting ON movie.id=movieid
        JOIN actor   ON actorid=actor.id
where movie.id in (select movieid from casting 
where actorid in 
(select id from actor where name = 'Julie Andrews'))
and ord = 1
```
####Actors with 15 leading roles
13.
Obtain a list, in alphabetical order, of actors who've had at least 15 starring roles.
```
select name 
from actor join casting
on actorid=actor.id
where ord =1
group by actor.name
having count(actor.name) >= 15
order by name
```

14.
List the films released in the year 1978 ordered by the number of actors in the cast, then by title
```
select title, count(actor.name) from
  movie JOIN casting ON movie.id=movieid
        JOIN actor   ON actorid=actor.id
where yr = 1978
group by title
order by count(actor.name) DESC , title 
```

15. List all the people who have worked with 'Art Garfunkel'.
```
select name from
  movie JOIN casting ON movie.id=movieid
        JOIN actor   ON actorid=actor.id 
where movieid in (select movieid from casting 
where actorid in 
(select id from actor where name = 'Art Garfunkel'))
and name <> 'Art Garfunkel'
order by name
```

## Self Join
Routes and stops
4.
The query shown gives the number of routes that visit either London Road (149) or Craiglockhart (53). Run the query and notice the two services that link these stops have a count of 2. Add a HAVING clause to restrict the output to these two routes.

```
SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
having count(*) = 2
```

5.
Execute the self join shown and observe that b.stop gives all the places you can get to from Craiglockhart, without changing routes. Change the query so that it shows the services from Craiglockhart to London Road.
```
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE b.stop=149
and a.stop = 53
```

6.
The query shown is similar to the previous one, however by joining two copies of the stops table we can refer to stops by name rather than by number. Change the query so that the services between 'Craiglockhart' and 'London Road' are shown. If you are tired of these places try 'Fairmilehead' against 'Tollcross'
```
SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'
and  stopb.name = 'London Road'
```

9.
Give a distinct list of the stops which may be reached from 'Craiglockhart' by taking one bus, including 'Craiglockhart' itself, offered by the LRT company. Include the company and bus no. of the relevant services.
```
SELECT DISTINCT s1.name,a.company,a.num FROM route a JOIN route b
ON (a.company = b.company AND a.num = b.num) JOIN stops s1 ON a.stop = s1.id
JOIN stops s2 ON b.stop = s2.id WHERE s1.name = 'Craiglockhart' or s2.name = 'Craiglockhart'
```
#### NSS Tutorial
Scores for Institutions in Manchester
7.
Show the average scores for question 'Q22' for each institution that include 'Manchester' in the name.

The column score is a percentage - you must use the method outlined above to multiply the percentage by the response and divide by the total response. Give your answer rounded to the nearest whole number.

```
SELECT institution,
round(sum(score * response / 100) / sum(response) * 100,0)
FROM nss
WHERE question='Q22'
AND (institution LIKE '%Manchester%')
GROUP BY institution;
```

Number of Computing Students in Manchester
8.
Show the institution, the total sample size and the number of computing students for institutions in Manchester for 'Q01'.
```
SELECT institution, SUM(sample), 
(SELECT sample FROM nss y
WHERE subject='(8) Computer Science'
AND x.institution = y.institution
AND question='Q01') 
AS comp
FROM nss x
WHERE question='Q01'
AND (institution LIKE '%Manchester%')
GROUP BY institution;
```
