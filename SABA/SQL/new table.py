# import pymysql as py
# Data=py.connect(
#     host='localhost',
#     user='root',
#     passwd='livewire'
# )
# a=Data.cursor()
# # a.execute('create database details ')
# c=py.connect(
#      host='localhost',
#     user='root',
#     passwd='livewire',
#     database='details'
# )
# e=c.cursor()

# # e.execute('create table employee (sno int ,sname varchar(100),age int ,salary int)')
# e.execute("insert into employee(sno,sname,age,salary)values(1,'john',23,15000),(2,'ravi',24,20000),(3,'velu',22,30000),(4,'kavin',30,50000)")
# e.execute('select * from employee')
# print(e.fetchall())
# c.commit()


import pymysql as sql
info=sql.connect(
    host='localhost',
    user='root',
    passwd='livewire'
)
b=info.cursor()
# b.execute('create database information')
n=sql.connect(
    host='localhost',
    user='root',
    passwd='livewire',
    database='information'
)
u=n.cursor()
# u.execute("create table student(sno int,sname varchar(100),marks int,grade varchar(10))")
u.execute("insert into student(sno,sname,marks,grade)values(1,'john',67,'B'),(2,'abdul',78,'B+'),(3,'akshay',95,'O'),(4,'ravi',88,'A')")
u.execute('select * from student')
print(u.fetchall())
n.commit()