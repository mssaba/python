import pymysql as a

D=a.connect(
    host='localhost',
    user='root',
    passwd='livewire',
    database='data')
c= D.cursor()
c.execute('select * from employee')
print(c.fetchall())

# c.execute('create table salary (sal int)')
c.execute('insert into salary(sal)values(25000)')
c.execute('select * from salary' )
print(c.fetchall())