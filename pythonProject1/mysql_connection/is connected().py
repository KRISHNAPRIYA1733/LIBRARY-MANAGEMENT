import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005")
if mydb.is_connected():
    print("connected successfully...")