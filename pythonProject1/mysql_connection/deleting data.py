import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
query="""
    delete from employee where id=5
"""
obj.execute(query)
mydb.commit()

query="""
    select * from employee
"""
obj.execute(query)
result=obj.fetchall()
for i in result:
    print(i)