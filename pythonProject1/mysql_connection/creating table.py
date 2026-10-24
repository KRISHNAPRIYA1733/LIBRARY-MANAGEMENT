import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
query="""create table employee(id int primary key,name varchar(200),place varchar(20),
company varchar(100),age int,salary int) """
obj.execute(query)
print("table created...")