import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
employees=[
    (6,"rahul","idukki","luminar",22,32000),
    (7,"gayathri","pathanamthitta","infosys",31,33000)
]
query="""
    insert into employee(id,name,place,company,age,salary)
    values(%s,%s,%s,%s,%s,%s)
"""
obj.executemany(query,employees)
mydb.commit()
#(id,name,place,company,age,salary)