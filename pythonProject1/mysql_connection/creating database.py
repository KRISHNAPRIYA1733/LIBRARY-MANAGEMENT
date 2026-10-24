import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005")
mycursor=mydb.cursor()
# mycursor.execute("create database companydb")
# print(mycursor.fetchall())
print("database created successfully..")
mycursor.execute("show databases")
print(mycursor.fetchall())