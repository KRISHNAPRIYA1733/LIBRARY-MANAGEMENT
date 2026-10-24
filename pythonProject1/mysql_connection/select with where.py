import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
query="select * from employee where id=3"
obj.execute(query)
print(obj.fetchone())

query="select * from employee where company='luminar'"
obj.execute(query)
print(obj.fetchall())

query="select * from employee where place='kochi'"
obj.execute(query)
print(obj.fetchall())