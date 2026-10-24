import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
id=int(input("enter your id:"))
name=input("enter your name:")
place=input("enter your place:")
company=input("enter your company:")
age=int(input("enter your age:"))
salary=int(input("enter your salary:"))

query="""
    insert into employee(id,name,place,company,age,salary)
    values(%s,%s,%s,%s,%s,%s)
"""
values= (id,name,place,company,age,salary)
obj.execute(query,values)
mydb.commit()
print("value inserted successfully")

obj.execute("select * from employee")
result=obj.fetchall()
for i in result:
    print(i)


