# -*- coding:utf-8 -*-
# @Time    : 2022/6/28 18:22
# @File    : mysql_knowledge.py
# Author: lee


# 不会的题目
# 4




"""
1.列举常见的关系型数据库和非关系型数据库


关系型数据库：复杂的数据结构归结为简单的二元关系，即二维表格形式，
            不是excel，但是和excel的形式很像

    mysql：大中小企业广泛使用
    sqlserver：只能在Windows系统下运行
    oracle： 传统大企业、大公司、政府、金融、证券等。

非关系型数据库： Not only sql
    不是否定关系型数据库，而是作为关系型数据库的补充
    为了高性能、高并发而生，忽略影响高性能，高并发的功能

        redis --- 是一个高性能的key-value数据库
         mongodb

"""



"""
2.Mysql常见数据库引擎及区别 --- mysql 中的概念
    1.引擎的概念只在 mysql 中存在
    2.Mysql 中数据是以表的形式存储的，引擎可以理解为表的类型
    +
    
    
    MyISAM
    InnoDB
    
    InnoDB Mysql 5.5 开始的默认引擎
            1.公司中最常用，也是最好用的引擎
            2.只存两个文件：1.表结构 2.数据、搜索目录 这两个文件
            3.支持事务（四个事务隔离级别），支持行级锁
            4.InnoDB对硬件资源要求还是比较高的
            
            
    MyISAM 
           1.的效率较高，但是 InnoDB 还有很多其他的功能
           2.存三个文件：1.表结构 2.数据 3搜索目录 这两个文件
           3.不支持事务，支持表级锁
           4.读取速度尽快，相对占用资源较少

    Memory：--- 读取最快
            将所有数据保存再RAM中


show engines；#查看MySQL所有的引擎

show variables like "storage_engine%"; 
# 查看当前正在使用的引擎


"""




"""
3.简述事务及其特性 --- 逻辑工作单位

事务是用户定义的一个数据库操作序列，这些操作要么不做，要么全做
是不可分割的的工作单位


    原子性：
        事务是数据库的逻辑工作单位，事务中的各种操作要么做要么不做
    
    一致性：
        事务执行的结果必须是使数据库从一个一致性状态到另外一个一致性状态
    
    隔离性：
        并发执行的各个事务是不能互相干扰的
    
    永久性（持续性）：
        一旦事务提交之后，他对数据库中的数据的改变就是永久性的，接下来的
        其他操作或者故障不应该对其执行结果有任何影响

"""






"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! （不会）

4.简述触发器、函数、视图和存储过程

    *************************************
        触发器
            触发器是一个特殊的存储过程，它是MySQL在insert、
            update、delete的时候自动执行的代码块
        mysql 触发器
        https://blog.csdn.net/A496608119/article/details/123277898
        
        视图
            视图是由查询结果形成的一张虚拟表，
            是表通过某种运算得到的一个投影
        
        存储过程
            把一段代码封装起来，当要执行这一段代码的时候，
            可以通过调用该存储过程来实现（经过第一次编译后再次调用不需要再次编译，
            比一个个执行sql语句效率高）
        mysql 触发过程
        https://blog.csdn.net/weixin_45970271/article/details/124180709
    *************************************

    函数：
        MySQL中提供了许多内置函数，还可以自定义函数（实现程序员需要sql逻辑处理）
        自定义函数
        https://blog.csdn.net/weixin_43763336/article/details/124141142



    触发器和存储过程的区别
    same
        1.触发器是一种特殊的存储过程
        2.触发器、存储过程，都是一个能够完成特定功能的，存储在数据库服务上的sql片段
    difference
        1.触发器不需要调用，当对数据库中的数据 执行 DML 操作的时候会自动触发 sql 片段，无需手动调用
        2.存储过程调用时 需要调用 sql 片段





"""






"""
5.mysql索引种类
    
    
    普通索引 index # 仅加速查询
    主键索引 primary key == not nul + unique
    唯一索引 unique
    组合索引 多列值组成一个索引 
    全文索引 fulltext
    


"""





"""
6.索引再什么情况下遵循最左前缀的规则

        联合索引
            #  从数据块的左边开始匹配，在匹配右边的
            #  当b+树的数据项是复合的数据结构，
            
                比如(name,age,sex)的时候，
                
                ***b+数是按照从左到右的顺序来建立搜索树的***
                
                    优先比较name来确定下一步的所搜方向，
                    如果name相同再依次比较age和sex，最后得到检索的数据；
                    
                    条件是 age, sex  的情况，索引失效
    """






"""
7.Mysql常见的函数

    AVG()
    SUM()
    MAX()
    MIN()
    COUNT()

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ROUND(x)：返回参数x的四舍五入的一个整数
TRIM(str)：去除字符串两边的空白


"""






"""
8.列举创建索引但是无法命中索引的情况

    1.or 连接的条件 不会命中索引
    2.联合索引，条件不是第一个联合索引中的字段
    3.like 匹配 以 % 开头
    4.字段类型错误，不会命中索引 ------------------
    5.如果列类型是字符串，那一定要在条件中将数据使用引号引用起来,否则不使用索引 -----------
    6.如果mysql估计使用全表扫描要比使用索引快,则不使用索引


"""








"""
！！！！！不太会的

9.数据库的导入与导出命令
    **************************************************

    导出(mysqldump)
    
        导出数据和表结构
                mysqldump -uroot -p dbname > dbname .sql
        
        只导出表结构
                mysqldump -uroot -p -d dbname > dbname .sql
    
    导入
            mysql -u用户名 -p密码 数据库名 < 数据库名.sql

    **************************************************



"""






"""
10.你了解哪些数据库优化方案

    1. 减少数据的访问，创建并正确使用索引 ****
        1.尽量使用区分度大的字段创建索引
        2. = 和 in 可以乱序 ****
        3.索引列不能参与计算 保持列“干净” ****
        4.or不会命中索引
        5.最左前缀匹配原则
    
    
    2.返回更少的数据 ****
        数据分页处理
        只返回需要的字段
    
    
    3.减少交互次数 ****
        使用存储过程
        优化业务逻辑
    
    
    4.减少服务器的cpu运算 ****
        使用绑定变量
        合理使用排序
        减少比较操作
        大量复杂运算在客户端处理
    
    
    5.利用更多资源 ****
        客户端多进程访问
        数据库并行处理


"""







"""
11.char和varchar的区别

    1.
        varchar 长度不固定
        char 长度固定
    2.
        char 效率高于 varchar


"""







"""
12.MySQL执行计划的作用和使用方法

    用来进行查询分析，
    比如整个查询涉及多少行，使用哪些索引，运行时间等
    
    explain

"""





"""
13.什么是索引合并
    1.把几个索引合的范围扫描合并成一个索引
    2.索引合并的时候， 对索引
                        先并集再交集 或者
                        先交集在并集的  以便合称为一个索引
                        
    3.索引只能是一个表的，不能对多表进行索引合并
    
"""





"""

！！！！！！！！不太会！！！！！！！


14.为什么数据很大的时候使用limit offset分页时，
越往后翻速度越慢，如何优化？

    当 使用 limit 分页时，limit 1000, 20
    含义是： 满足查询条件的10020的查询结果中去掉 前1000行，返回后20行
    花费了大量时间在扫描上
    
    ********************************
    优化方法：
        1.当数据库过于庞大的时候， limit offset, length
        offset 过大的时候，sql查询语句会非常慢，需要增加 order by
        并且 order by 字段需要增加索引
        
        
        2.如果使用子查询去优化LIMIT的话，则子查询必须是连续的，
        某种意义来讲，子查询不应该有where条件，
        where会过滤数据，使数据失去连续性
    


"""







"""
15.什么是覆盖索引 --- 又称为索引覆盖

    1. 辅助索引
    2. where 查询的条件 命中了辅助索引，
    直接从b+树中叶子节点中直接获取到了数据
    
    
    
    
ps: 备注知识：


    主键索引 --- 聚集索引
        聚集索引（clustered index）就是按照每张表的主键构造一棵B+树，
            同时叶子结点存放的即为整张表的行记录数据，
    
    
    辅助索引：除了聚集索引外其他索引都是辅助索引
        （Secondary Index，也称为非聚集索引）
         （unique key啊、index key啊）
    
    
        相同点：不管是聚集索引还是辅助索引，其内部都是B+树的形式，
            即高度是平衡的，叶子结点存放着所有的数据。

        不同点：叶子结点存放的是否是一整行的信息**


    
    
    
    
    

"""






"""
！！！！！！！！！！！！！！！！！！！！！！！！！

16.简述数据库的读写分离
    
    详细介绍（了解）
    https://www.cnblogs.com/0zcl/p/7141459.html

    读写分离就是指 主服务器上修改，数据会同步到从服务器上，
    从服务器只能提供读取服务，不能写入，实现备份的同时实现了数据库的优化
    以及提升了服务器的安全

"""






"""
17.简述数据库分库分表 ！！！！！！！！！！！！！！！！

https://www.cnblogs.com/butterfly100/p/9034281.html


垂直切分
    垂直分库：
        就是根据业务耦合性，
        将关联度低的不同表存储在不同的数据库
    垂直分表：
        基于数据库中的"列"进行，某个表字段较多，
        可以新建一张扩展表，
        将不经常用或字段长度较大的字段拆分出去到扩展表中。


横向切分：
    水平切分分为库内分表和分库分表，是根据表内数据内在的逻辑关系，
    将同一个表按不同的条件分散到多个数据库或多个表中，
    每个表中只包含一部分数据，从而使得单个表的数据量变小，达到分布式的效果。



"""






"""
！！！！！！！！！！！！！！！！！！！！！！！！！

18.数据库锁的作用

https://blog.csdn.net/zhangzhetaojj/article/details/81559583

    锁分为三种：乐观锁，悲观锁和共享锁
        数据库和操作系统一样，是一个多用户使用的共享资源。
        当多个用户并发地存取数据 时，
        在数据库中就会产生多个事务同时存取同一数据的情况。
        若对并发操作不加控制就可能会读取和存储不正确的数据，
        破坏数据库的一致性。加锁是实现数据库并 发控制的一个非常重要的技术。
        在实际应用中经常会遇到的与锁相关的异常情况，
        当两个事务需要一组有冲突的锁，而不能将事务继续下去的话，
        就会出现死锁，严 重影响应用的正常执行。


"""






"""
！！！！！！！！！！！！！！！！！！！！！！！！！
19.MySQL的半同步复制原理

    半同步复制，
        介于异步复制和全同步复制之间，
        主库在执行完客户端提交的事务后不是立刻返回给客户端，
        而是等待至少一个从库接收到并写到relay log中才返回给客户端。
        相对于异步复制，半同步复制牺牲了一定的性能，提高了数据的安全性。

    异步复制，
        MySQL默认的复制是异步的，
        主库在执行完客户端提交的事务后会立即将结果返给给客户端，
        并不关心从库是否已经接收并处理。
        原理最简单，性能最好，但是主从之间数据不一致的概率很大。

    全同步复制，
        指当主库执行完一个事务，
        所有的从库都执行了该事务才返回给客户端。
        因为需要等待所有从库执行完该事务才能返回，
        所以全同步复制的性能必然会收到严重的影响。



"""






"""
20.MySQL的增删改查

    增
        insert into table_name(字段1, ..) values
            (value1,...),
            (value1,...),
            (value1,...);
            
        
    删
        delete from table_name where 条件    
        trancte table table_name # 清空表的数据
    
    
    改 # ********
        update table_name set 字段 = value where 条件;
    
    查
        
        
        查询所有字段
        语法：select * from 表名；
        
        
        按条件查询
        语法：select 字段名1，字段名2，… from table_name where 条件

        
        
        带IN关键字的查询
        语法：select 字段名1，字段名2，… from table_name where 字段1 in ..;
        
        
        
        带 BETWEEN AND 关键字的查询
        语法：select id,name from table_name where id between  and ;
        
        
        
        空值查询
        语法：select * | 字段名1，字段名2，… from 表名 where 字段名 is [ NOT ] null
        
        
        带 DISTINCT 关键字的查询
        语法：SELECT DISTINCT 字段名 FROM 表名；

        
        
        带 LIKE 关键字的查询
        语法：SELECT * | 字段名1，字段名2，… FROM 表名 WHERE 字段名 [ NOT ] LIKE ‘匹配字符串’;
        注意：%表示匹配任意长度的字符串，_表示匹配单个字符串

        
        
        
        带 AND 关键字的多条件查询
        语法：SELECT * | 字段名1，字段名2，… FROM 表名 WHERE 条件表达式1 AND 条件表达式2 [ … AND 条件表达式 n ];
        带 OR 关键字的多条件查询
        语法：SELECT * | 字段名1，字段名2，… FROM 表名 WHERE 条件表达式1 OR 条件表达式2 [ … OR 条件表达式 n ];
        AND和OR一起使用时，AND的优先级高于OR
        
        
        聚合函数
        COUNT()函数：统计记录的条数
        语法：SELECT COUNT(*) FROM 表名举例：
        命令：SELECT COUNT(*) FROM student2;
        
        
        SUM()函数：求出表中某个字段所有值的总和
        语法：SELECT SUM(字段名) FROM 表名；
        命令：SELECT SUM(grade) FROM student2;
        
        AVG()函数：求出表中某个字段所有值的平均值
        语法：SELECT AVG(字段名) FROM 表名；
        命令：SELECT AVG(grade) FROM student2;
        
        MAX()函数：求出表中某个字段所有值的最大值
        语法：SELECT MAX(字段名) FROM 表名；
        命令：SELECT MAX(grade) FROM student2;
        
        MIN()函数：求出表中某个字段所有值的最小值
        语法：SELECT MIN(字段名) FROM 表名；
        命令：SELECT MIN(grade) FROM student2;
        
        对查询结果进行排序
        语法：SELECT 字段名1，字段名2，… FROM 表名 ORDER BY 字段名1 [ ASC | DESC ],字段名2 [ ASC | DESC ]
        (升序)命令：SELECT * FROM student2 ORDER BY grade;
        (降序)命令：命令：SELECT * FROM student2 ORDER BY grade DESC;
        
        
        
        分组查询
        语法：SELECT 字段名1，字段名2，… FROM 表名 GROUP BY 字段名1，字段名2，… [ HAVING 条件表达式 ];
        单独使用 GROUP BY 进行分组
        命令：SELECT * FROM student2 GROUP BY gender;
        
        
        
        GROUP BY 和聚合函数一起使用
        命令：SELECT COUNT(*) ,gender FROM student2 GROUP BY gender;
        GROUP BY 和 HAVING 关键字一起使用
        命令：SELECT sum(grade),gender FROM student2 GROUP BY gender HAVING SUM(grade) < 300;
        
        
        
        使用 LIMIT 限制查询结果的数量
        语法：SELECT 字段名2，字段名2，… FROM 表名 LIMIT [ OFFSET ,] 记录数
        (从0开始的4条)命令：SELECT * FROM student LIMIT 4;
        (从第五条开始的4条)命令：SELECT * FROM student2 ORDER BY grade DESC LIMIT 4,4;
        为表和字段取别名
        语法：SELECT * FROM 表名 [ AS ] 别名；
        命令：SELECT * FROM student2 AS s WHERE s.gender='女';
        
        
        为字段取别名
        语法：SELECT 字段名 [ AS ] 别名 [ ,字段名 [AS] 别名，…] FROM 表名 ；
        命令：SELECT name AS stu_name,gender AS stu_gender FROM student2;

"""








"""
21.MySQL的建表语句

create table table_name(
    ...
    
)engine myisam charset utf8; # 这个确实不太知道


"""







"""
22.MySQL如何创建索引


    alter table table_name add index index_name()
    alter table table_name add unique key u_name()
    alter table table_name add primary key()
    
    # CREATE INDEX可对表增加普通索引或UNIQUE索引
        creat index index_name on table_name()
        creat unique index_name on table_name()
    
"""







"""
23.简述SQL注入原理，以及如何在代码层面防止sql注入

原因：
    SQL语句的拼接中，一些含特殊字符的变量在拼接时破坏了SQL语句的结构
    用户输入的数据意外的成为了被执行的代码

    举例
        sql = "select * from userinfo where username='%s' and password='%s';"%(uname,pword)
        
        >>>请输入用户名：chao' -- xxx
        -- sql 中表示的是注释的含义
    
    
    用户输入数据：
    1."Web前端$_POST,$_GET获取的数据，
    2.从数据库获取的数据，
    3.程序猿无意中使用的特殊字符串。 
    
    
    
    

规避方法：
    1.解析协议层面上完全规避SQL注入
    2.字符串转义（不要在sql中拼接字符） 
    res = cursor.execute(sql, [将要传入的参数])
    # query作为sql模板，args为将要传入的参数 execute(query, args=None)


"""







"""
24.使用python将数据库的student表中的数据写入db.txt

***************************************************

import pymysql

connect=pymysql.Connect(
host='',
port=,
user='',
passwd='',
db='',
charset='', # 编码
) # 连接数据库


cursor = connect.cursor()     # 创建游标
sql = 'select * from student' # sql 语句
cursor.execute(sql)         # 执行
student = cursor.fetchall()


with open('db.txt','w') as f:
    for student in students:
        f.write(student)

cursor.close()
connect.close()


***************************************************
    

"""




"""
25.简述left join和right join的区别
    
    左右连接很相似，只是左右的位置不同而已
    
    left join
        返回包括 左表中的全部记录 与 右表中连接字段相等 的记录
        
         
    right join
        返回包括 右表中的全部记录 与 左表中连接字段相等 的记录

"""




"""
26.索引有什么作用，有哪些分类，有什么好处和坏处？
    作用：
        为了增加查询速度，提高系统性能
    
    
    分类：
        普通索引
        
        主键索引
            有一列或列组合，其值唯一标识表中的每一行。
        
        唯一索引
            不允许其中任何两行具有相同索引值的索引。
            
        全文索引
        
        
        聚集索引
        辅助索引
    
    
    好处：**************************************
        1.加快查询速度
        4.利用索引的唯一性来控制记录的唯一性 (约束条件)
        2.可以加速表与表之间的连接 ！！！！
        3.降低查询中分组和排序的时间 ！！！
    
    坏处：
        1.存储索引占用磁盘空间
        2.查询加快，但是写入变慢
        3.执行数据修改操作(INSERT、UPDATE、DELETE)产生索引维护


"""




"""
27.mysql慢日志

    MySQL的慢查询日志是MySQL提供的一种日志记录，
    它用来记录在MySQL中响应时间超过阀值的语句，
    具体指运行时间超过long_query_time值的SQL，
    则会被记录到慢查询日志中。
"""





"""
28.慢查询优化的基本步骤 *******************************

    0.先运行看看是否真的很慢，注意设置SQL_NO_CACHE
        select SQL_CACHE count(*) from ...;
        # 查询的时候记得不使用缓存
        
    1.where条件单表查，锁定最小返回记录表。
        这句话的意思是把查询语句的where都应用到   表中返回的记录数最小的   表开始查起，
        单表每个字段分别查询，看哪个字段的区分度最高
    
    2.explain查看执行计划，是否与1预期一致（从锁定记录较少的表开始查询）
    
    3.order by limit 形式的sql语句让排序的表优先查
    
    4.了解业务方使用场景
    
    5.加索引时参照建索引的几大原则
    
    6.观察结果，不符合预期继续从0分析

"""


"""
建立索引的原则有哪些？

    1.选择区分度大的字段创建索引
    
    2.不要建立过多的索引。因为索引本身会占用存储空间
    
    3.建立索引时遵照最左匹配原则
    
    4.建立唯一索引。唯一索引能够更快速地帮助我们进行数据定位；
    
    5.为经常需要进行查询操作的字段建立索引
    
    6.对经常需要进行排序、分组以及联合操作的字段建立索引
    
    7.尽量考虑字段值长度较短的字段建立索引
            如果字段值太长，会降低索引的效率。
    

"""

