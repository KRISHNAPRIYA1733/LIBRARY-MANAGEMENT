import mysql.connector
#creates or gets a mysql connection object
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005")
print(mydb)