import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005")
obj=mydb.cursor()
obj.execute("select version()")
print(obj.fetchone())

obj.execute("show databases")
print(obj.fetchall())