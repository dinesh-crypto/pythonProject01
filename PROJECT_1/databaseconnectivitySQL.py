import pymysql

db = pymysql.connect(host="localhost", user='root', password='', database='dinesh')

x = db.cursor()
x.execute("use dinesh")
try:
    x.execute("create table stud(id int,name varchar(30), age int) ")
except Exception as e:
    print(e)

id = int(input("Enter your id:"))
name = input("Enter your name: ")
age = int(input("Enter your age: "))

x.execute("INSERT INTO stud(id, name, age) VALUES (%s, %s, %s)", (id, name, age))
db.commit()
x.execute("select * from stud")
c = x.fetchall()
print(c)
db.close()