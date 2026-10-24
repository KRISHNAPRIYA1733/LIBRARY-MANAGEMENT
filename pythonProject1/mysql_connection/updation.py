import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
query="""
    update employee set place="kannur"
    where id=3
"""
obj.execute(query)
mydb.commit()
print("data updated successfully")

print("..after updation..")
query="""
    select * from employee where id=3
"""
obj.execute(query)
print(obj.fetchone())