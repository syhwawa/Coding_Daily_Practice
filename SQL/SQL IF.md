### IF 表达式
```Python
IF( expr1 , expr2 , expr3 )
```

expr1 的值为 TRUE，则返回值为 expr2 
expr1 的值为FALSE，则返回值为 expr3

如下：
```Python
SELECT IF(TRUE,1+1,1+2);
-> 2

SELECT IF(FALSE,1+1,1+2);
-> 3
```
 
SELECT IF(STRCMP("111","222"),"不相等","相等");
-> 不相等
那么这个 IF 有啥用处呢？举个例子： 
查找出售价为 50 的书，如果是 java 书的话，就要标注为 已售完 

那么对应的SQL语句该怎样去写呢？

select *,if(book_name='java','已卖完','有货') as product_status from book where price =50

### IFNULL 表达式

判断第一个参数expr1是否为NULL：

　　　　如果expr1不为空，直接返回expr1；

　　　　如果expr1为空，返回第二个参数 expr2   

常用在算术表达式计算和组函数中，用来对null值进行转换处理(返回值是数字或者字符串)

在 expr1 的值不为 NULL的情况下都返回 expr1，否则返回 expr2，如下：

```Python
SELECT IFNULL(NULL,"11");
-> 11
 
SELECT IFNULL("00","11");
-> 00
```
NULLIF 表达式

NULLIF(expr1,expr2)：如果两个参数相等则返回NULL，否则返回第一个参数的值expr1


### 3、在SQL语句中实现“if-then-else”逻辑计算功能

　　有两种形式：simple case和searched case

1）simple case的语法结构：


```Python
CASE  value
 
    WHEN  [compare_value] THEN  result
 
    [WHEN [compare_value] THEN  result ...] 
 
    [ELSE  result]  END
```

语义：

　　将case后面的值value分别和每个when子句后面的值compare_value进行相等比较：

　　　　如果一旦和某个when子句后面的值相等则返回相应的then子句后面的值result；

　　　　如果和所有when子句后面的值都不相等，则返回else子句后面的值；

　　　　如果没有else部分则返回null。

注意：

　　①value可以是字面量、表达式或者列名

　　②CASE表达式的数据类型取决于跟在then或else后面的表达式的类型


```Python
mysql> select userid,case salary                                             
    -> when 1000 then 'low'
    -> when 2000 then 'med'
    -> when 3000 then 'high'
    -> else '无效值' end salary_grade
    -> from salary_tab;
+--------+--------------+
| userid | salary_grade |
+--------+--------------+
|      1 | low          |
|      2 | med          |
|      3 | high         |
|      4 | 无效值        |
|      5 | low          |
+--------+--------------+
```
2）searched  case的语法结构：

```Python
CASE
 
    WHEN [condition] THEN result
 
    [WHEN [condition] THEN result ...]
 
    [ELSE result]  END
```
语义：

　　如果某个when子句后面的条件condition为true，则返回相应的when子句后面的值result；

　　如果所有的when子句后面的条件condition都不为true，则返回else子句后面的值；

　　如果没有else部分则返回null。

```Python
mysql> select userid,case
    -> when salary<=1000 then 'low'
    -> when salary=2000 then 'med'
    -> when salary>=3000 then 'high'
    -> else '无效值' end salary_grade
    -> from salary_tab;
+--------+--------------+
| userid | salary_grade |
+--------+--------------+
|      1 | low          |
|      2 | med          |
|      3 | high         |
|      4 | 无效值        |
|      5 | low          |
+--------+--------------+
```
