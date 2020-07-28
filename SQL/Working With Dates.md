## SQL Dates
__The most difficult part when working with dates is to be sure that the format of the date you are trying to insert, matches the format of the date column in the database.__

As long as your data contains only the date portion, your queries will work as expected. However, if a time portion is involved, it gets more complicated.

#### SQL Date 数据类型
MySQL 使用下列数据类型在数据库中存储日期或日期/时间值：

DATE - 格式：YYYY-MM-DD
DATETIME - 格式：YYYY-MM-DD HH:MM:SS
TIMESTAMP - 格式：YYYY-MM-DD HH:MM:SS
YEAR - 格式：YYYY 或 YY
SQL Server 使用下列数据类型在数据库中存储日期或日期/时间值：

DATE - 格式：YYYY-MM-DD
DATETIME - 格式：YYYY-MM-DD HH:MM:SS
SMALLDATETIME - 格式：YYYY-MM-DD HH:MM:SS
TIMESTAMP - 格式：唯一的数字

MySQL Date 函数
下面的表格列出了 MySQL 中最重要的内建日期函数：

函数	描述
NOW()	返回当前的日期和时间
CURDATE()	返回当前的日期
CURTIME()	返回当前的时间
DATE()	提取日期或日期/时间表达式的日期部分
EXTRACT()	返回日期/时间的单独部分
DATE_ADD()	向日期添加指定的时间间隔
DATE_SUB()	从日期减去指定的时间间隔
DATEDIFF()	返回两个日期之间的天数
DATE_FORMAT()	用不同的格式显示日期/时间
