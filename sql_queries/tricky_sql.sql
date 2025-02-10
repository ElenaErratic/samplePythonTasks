/* A number of tricky SQL tasks with sample datasets to test the solution.
Test the results using, e.g., https://www.db-fiddle.com/ SQLite v3.39	*/

------Determine the client who has the highest-paying order.
create table orders(id int, client_id int, order_dt date, order_sum int);
insert into orders values(1, 2, '2022-01-01', 1000),
	(2, 2, '2022-01-02', 10000),
	(3, 1, '2022-01-03', 1000),
	(4, 3, '2022-01-04', 500),
	(5, 4, '2022-01-05', 1500);

select client_id
from orders
where order_sum >= (select max(order_sum) from orders);


-------Find the clients whose average monthly payment is more than 10000 and who have at least 5 payments that
--exceed 5000.
create table CLIENTS(client int, product text, payment int); -- Oracle: string
insert into CLIENTS values(1, 'Кредит1', 10000),
(1, 'Кредит2', 7000),
(1, 'Карта1', 6000),
(1, 'Ипотека1', 50000),
(1, 'Кредит3', 5500),
(1, 'Кредит4', 5600),
(2, 'Кредит1', 30000),
(2, 'Кредит2', 40000),
(2, 'Карта1', 4000),
(2, 'Карта2', 4000),
(2, 'Карта3', 4000),
(2, 'Карта4', 4000),

(3, 'Кредит1', 10000),
(3, 'Кредит2', 7000),
(3, 'Карта1', 6000),
(3, 'Кредит3', 5500),
(3, 'Кредит4', 5600),
(3, 'Кредит5', 6000),	
--(3, 'Ипотека1', 50000)

(4, 'Кредит1', 30000),
(4, 'Кредит2', 40000),
(4, 'Карта1', 5100),
(4, 'Карта2', 5100),
(4, 'Карта3', 5100),
(4, 'Карта4', 100),
(4, 'Карта5', 100),
(4, 'Карта6', 100),
(4, 'Карта7', 100),
(4, 'Кредит3', 10000)

	
--first solution
select client
from CLIENTS
where payment > 5000
group by client
having count(payment) > 5
INTERSECT
select client
from CLIENTS
group by client
having avg(payment) > 10000;

--second solution
select client
from CLIENTS
where client in  (
      select client
      from CLIENTS
      where payment > 5000
      group by client
      having count(payment) > 5)
group by client
having avg(payment) > 10000;

--third solution
select cc.client
from CLIENTS c
right join CLIENTS cc
on c.client = cc.client and c.product = cc.product
and c.payment > 5000
group by cc.client
having count(c.payment) > 5 and avg(cc.payment) > 10000;

--wrong simple solution 
/*avg payment of client 4 is 9570. this client should not be included.
The result should not include the clients who have avg payment above 10K of only payments that are above 5k - all payments should be counted*/
select client
from CLIENTS
where payment > 5000
group by client
having count(payment) > 5  and avg(payment) > 10000;


------Select the maximum monthly payment per client and specify the product.
--For Oracle:
WITH max_p AS
(
select client, max(payment) as payment
from CLIENTS
group by client
)
                 
select c.client, c.product, c.payment
from CLIENTS c
join max_p m
	on m.client=c.client
	and m.payment=c.payment;

--For most other dialects:
select client, product, max(payment) as payment
from CLIENTS
group by client;


------Calculate the average payment per client. The data may be null for some clients.
select client, avg(ifnull(payment,0)) 
from clients 
group by client
order by client;
	
--also possible: coalesce; in other dialects: isnull; nvl (oracle)
--Compare: It is also possible to use 'over partition by' but without 'group by' it would yield all rows of the table, whereas adding 'group by'
--to this function collapses rows to show only distinct grouping values.


------Calculate the daily running total (balance).
create table OPERATIONS(oper_dt date, value int);
insert into OPERATIONS values('2022-01-01', 1000),
	('2022-01-02', 1000),
	('2022-01-03', 1000),
	('2022-01-04', -500),
	('2022-01-05', -500);

--first solution
select oper_dt, value,
	sum(value) over (order by oper_dt) as balance -- (order by oper_dt ROWS UNBOUNDED PRECEDING)
from OPERATIONS;

--second solution
select o.oper_dt, o.value, sum(op.value) as balance
from OPERATIONS o
join OPERATIONS op
	on o.oper_dt >= op.oper_dt
group by o.oper_dt, o.value;


------Count the sum of all positive and the sum of all negative numbers in a column.
select sum (case when value > 0
			then value end) as positive_numbers
	   , sum (case when value < 0 
       		then value end) as negative_numbers
		
from OPERATIONS;

/*
Задание "Средняя зп по больнице"

Есть таблица db со всеми сотрудниками фирмы

user_id - int32 - id сотрудника
boss_user_id - int32? - user_id руководителя этого сотрудника
payment - double - зарплата сотрудника в рублях

Напишите SQL запросы, которые отвечают на вопрос:
1. Какая средняя зп у руководителей? (руководитель - это тот, у которого есть хотя бы 1 подчиненный)
2. Сколько в среднем прямых подчиненных у руководителей?
3. У каких сотрудников зп выше, чем у их руководителей

Пример данных
userid bossid  payment
1       2      50000.0
5       2      60000.0
6       2      70000.0
7       2      90000.0
2       3      200000.0
*/


--Решение

--1
select avg(payment) as "Average Boss Payment"
from db
where user_id in (select distinct boss_user_id from db);

--2
select avg(s_count) as "Average Subordinate Count"
from (select boss_user_id, count(user_id) as s_count
        from db
        group by boss_user_id) db2;

---В некоторых случаях подойдет упрощенное решение (например, если у подчиненного всегда только один начальник):
select count(distinct bossid)/count(distinct userid) as "Average Subordinate Count"
	from db;

--3
select db1.user_id --, db1.payment "Subordinate Payment", db2.payment as "Boss Payment"
from db as db1, db as db2
where db1.boss_user_id = db2.user_id
  and db1.payment > db2.payment;



--TOP 3 earners
/*Find out who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three _unique_ salaries for that department.
*/
--Solution 1
WITH earners_rank AS
(
    SELECT departmentId, name, salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) dr
    FROM employee
),
top3_earners as
(
    SELECT * from earners_rank
    WHERE dr < 4
)
SELECT 
    dep.name "Department", 
    te.name "Employee", 
    te.salary "Salary"
FROM top3_earners te
JOIN department dep
ON dep.id=te.departmentId

--Solution2
select d.name as department , e1.name as employee, e1.salary as Salary
from employee e1 join department d on e1.departmentId = d.Id
where  3 > (select count(distinct (e2.Salary))
            from employee e2
            where e2.Salary > e1.Salary
            and e1.departmentId = e2.departmentId)


--SALARY RANKING
/*
Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.
Output: 
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
*/

select  
    'Low Salary' as category,
    ifnull(count(case when income < 20000 then 'Low Salary' end),0) as accounts_count
from accounts
UNION
select  
    'Average Salary' as category,
    ifnull(count(case when income >= 20000 and income <= 50000 then 'Average Salary' end),0) as accounts_count
from accounts
UNION
select  
    'High Salary' as category,
    ifnull(count(case when income > 50000 then 'High Salary' end),0) as accounts_count
from accounts
---Even better: COUNT(if(income<20000,1,null)) AS accounts_count
	

--Second Highest Salary
/*
Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null 
*/

WITH salary_ranking AS
(
    SELECT id, salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) dr
    FROM employee
)
select max(salary) as SecondHighestSalary -- max is needed at least in MySQL to return null properly if there are no matching values
from salary_ranking
where dr = 2

	
--Investments in 2016
/*
Table: Insurance
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

have the same tiv_2015 value as one or more other policyholders, and
are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.
*/

--solution1

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1

--solution2

WITH cities AS
(
select lat, lon, count(*) count
from insurance
group by lat, lon
),

tiv_2015_counts AS
(
    select tiv_2015, count(*) count
    from insurance
    group by tiv_2015
)

select round(sum(i.tiv_2016),2) as tiv_2016
from insurance i
join cities c
on i.lat = c.lat and i.lon = c.lon and c.count = 1
join tiv_2015_counts tc
on i.tiv_2015 = tc.tiv_2015 and tc.count > 1


