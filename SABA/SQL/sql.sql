create database data;
use data;
drop table employee;
create table employee(sno int ,sname varchar(100),age int );
insert into employee(sno,sname,age) values(4,'raju',28);

select * from employee;
select sname from employee where age>23;

SET SQL_SAFE_UPDATES = 0;
update employee set age=30 where sname='raju';
select max(age) as newdata from employee;
select min(age) from employee;
select count(age) from employee where age>23;
SELECT * FROM employee WHERE sname LIKE 'R%';
SELECT * FROM employee WHERE age BETWEEN 25 AND 30;

create table dept(dname varchar(100));
insert into dept(dname)values('hr'),('md'),('clerk'),('manager');
select*from dept



