#### Window Functions
You will learn about window functions and how to pass aggregate functions along a dataset. You will also learn how to calculate running totals and partitioned averages.

RANK()函数是一个Window函数，它为结果集的分区中的每一行分配一个排名。
分区中具有相同值的行将获得相同的排名。 分区中第一行的等级是1。 RANK()函数将绑定行的数量添加到绑定等级以计算下一行的等级，因此，等级可能不是连续的。
RANK()函数的语法如下所示：
RANK() OVER (
    [PARTITION BY partition_expression, ... ]
    ORDER BY sort_expression [ASC | DESC], ...
)
SQL
在这个语法中：

首先，PARTITION BY子句划分应用该函数的结果集分区的行。其次，ORDER BY子句指定应用该函数每个分区中行的逻辑排序顺序。
RANK()函数对于求解前N个和后N个报表很有用。
SQL Server RANK()说明首先，创建一个名为sales.rank_demo的新表，其中包含一列：
CREATE TABLE sales.rank_demo (
 v VARCHAR(10)
);
SQL
其次，向sales.rank_demo表中插入一些行：
INSERT INTO sales.rank_demo(v)
VALUES('A'),('B'),('B'),('C'),('C'),('D'),('E');
SQL
第三，从sales.rank_demo表中查询数据：
SELECT 
 v
FROM
 sales.rank_demo;
SQL
第四，使用ROW_NUMBER()为sales.rank_demo表的结果集中的行分配排名：
SELECT
 v,
 RANK () OVER ( 
 ORDER BY v 
 ) rank_no 
FROM
 sales.rank_demo;
SQL
执行上面查询语句，得到以下结果：

从输出中清楚地显示，第二和第三行接收相同的等级，因为它们具有相同的值B。第四和第五行得到等级4，因为RANK()函数跳过等级3并且它们也具有相同的值(4)。//原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/sqlserver/sql-server-rank-function.html

