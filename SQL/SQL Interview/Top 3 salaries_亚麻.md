```
Employee 
+----+-------+--------+--------------+
| Id | Name  | Sa1ary | DepartmentId |
+----+-------+--------+--------------+
|  1 | Joe   |  70000 |            1 |
|  2 | Henry |  80000 |            2 |
|  3 | Sam   |  60000 |            2 |
|  4 | Max   |  90000 |            1 |
|  5 | Janet |  69000 |            1 |
|  6 | Randy |  85000 |            1 |
+----+-------+--------+--------------+
 
Department 
+----+-------+
| Id | Name  | 
|  1 | IT    | 
|  2 | SALES | 
+----+-------+
```

Question:
https://stackoverflow.com/questions/35653431/how-to-select-the-top-3-salaries-of-the-department
```
SELECT 
      D.Name AS Department, 
      E.Name AS Employee, 
      E.Salary AS Salary,
      Count(E2.Salary) as Count_employees_who_earn_more
FROM Employee E 
INNER JOIN Department D 
ON E.DepartmentId = D.Id 
LEFT JOIN Employee E2 ON 
    e2.DepartmentId = E.DepartmentId
    AND E2.Salary > E.Salary
GROUP BY  D.Name , 
      E.Name , 
      E.Salary
```

