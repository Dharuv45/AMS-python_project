import sqlite3
db=sqlite3.connect("attendancesystem.db")
cr=db.cursor()
cr.execute('''create table Admin(Name varchar(32), Email varchar(32), Password varcharr(32))''')
cr.execute('''create table courses(courseid int, coursename varchar(32))''')
cr.execute('''create table teacher(eid int , name varchar(32), email varchar(32), Password  varchar(32), gender varchar(32))''')
cr.execute('''create table attendance (rollno int , course varchar(32), Date Date, Attendance varchar(32))''')
cr.execute('''create table student(rollno int , name varchar(32), email varchar(32), Password  varchar(32), gender varchar(32), course varchar(32))''')
db.commit()
db.close()
