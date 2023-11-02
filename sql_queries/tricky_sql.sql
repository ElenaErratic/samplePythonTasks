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
(2, 'Кредит1', 20000),
(2, 'Кредит2', 20000),

(3, 'Кредит1', 10000),
(3, 'Кредит2', 7000),
(3, 'Карта1', 6000),
(3, 'Кредит3', 5500),
(3, 'Кредит4', 5600),
(3, 'Кредит5', 6000)	
--(3, 'Ипотека1', 50000)
;


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

--3
select db1.user_id --, db1.payment "Subordinate Payment", db2.payment as "Boss Payment"
from db as db1, db as db2
where db1.boss_user_id = db2.user_id
  and db1.payment > db2.payment;
