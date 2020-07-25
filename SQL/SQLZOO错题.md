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
