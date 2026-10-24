import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
query="""select * from employee"""
obj.execute(query)
result=obj.fetchall()
for emp in result:
    print(emp)
print("...get the details of one employee..")
obj.execute("select * from employee")
employee=obj.fetchone()
print(employee)