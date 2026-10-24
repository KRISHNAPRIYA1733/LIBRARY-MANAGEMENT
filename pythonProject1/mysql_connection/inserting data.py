import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
query="""
    insert into employee(id,name,place,company,age,salary)
    values(1,"amal","aluva","TCS",25,30000),
    (2,"anisha","kochi","TCS",30,35000),
    (3,"karthika","palakkad","luminar",35,28000),
    (4,"midhin","kochi","infosys",24,29000),
    (5,"varun","malappuram","wipro",31,34000)
"""
obj.execute(query)
print("inserted successfully...")
mydb.commit()
#create table employee(id int primary key,name varchar(200),place varchar(20),
#company varchar(100),age int,salary int) """