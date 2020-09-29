Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You really love counting stuff. In fact, right now you're sitting on a meadow and counting all the legs you see there! There are some people, some dogs, and some cats on the meadow. You're pretty confident that each human has 2 legs and that cats and dogs have 4 legs each.

The information about all the creatures on the meadow is stored in the table creatures. It has the following structure:

id: the unique creature ID;
name: the creature's name;
type: the creature's type - "human", "cat", or "dog". This column has ENUM type.
You want to calculate the total number of legs in the meadow. Given the table creatures, build a new table that only contains one column summary_legs and has only one row with the total number of legs that you can see.

Example

For the following table creatures
```
id	name	type
1	Mike	human
2	Misty	cat
3	Max	dog
4	Tiger	human
the output should be

summary_legs
12
```
There are 2 humans, 1 cat, and 1 dog, so there are 2 * 2 + 1 * 4 + 1 * 4 = 12 legs in total.

[execution time limit] 10 seconds (mysql)



```SQL
DROP PROCEDURE IF EXISTS legsCount;
CREATE PROCEDURE legsCount()
    SELECT SUM(IF(type = 'human', 2, 4)) as summary_legs
    FROM creatures
    ORDER BY id;

```

```SQL

DROP PROCEDURE IF EXISTS legsCount;
CREATE PROCEDURE legsCount()
    SELECT ROUND ((sum((SELECT COUNT(name) FROM creatures WHERE type = 'human' GROUP BY type) * 2 + 
                (SELECT COUNT(name) FROM creatures WHERE type = 'cat' GROUP BY type) * 4 + 
                (SELECT COUNT(name) FROM creatures WHERE type = 'dog' GROUP BY type) * 4))/ COUNT(*), 0) as summary_legs
    FROM creatures
    ORDER BY id;

```
