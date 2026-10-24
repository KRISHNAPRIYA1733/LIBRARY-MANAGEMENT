import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="companydb")
obj=mydb.cursor()
#
# query="""
#     create table student(id int primary key,name varchar(50),age int,place varchar(50),course varchar(50),
#     mobile bigint unique,college varchar(50))
# """
# obj.execute(query)
#
# query="""
#     insert into student(id,name,age,place,course,mobile,college)
#     values(1,"amal",20,"kochi","BCA",3835478907,"ABC college"),
#     (2,"anu",20,"kochi","BTECH",3835411907,"ABC college")
# """
# obj.execute(query)
# mydb.commit()
# print("inserted  successfully")

#INSERT DATA..........................
query="""insert into student(id,name,age,place,course,mobile,college)
values(%s,%s,%s,%s,%s,%s,%s)"""
values=(10,"anjana",23,"aluva","mca",3536789790,"bmc college")
# obj.execute(query,values)
mydb.commit()
print("new student inserted")

#SELECT DATA..........................
obj.execute("select * from student")
result=obj.fetchall()
for i in result:
    print(i)

#UPDATE DATA..........................
obj.execute("update student set age=25 where id=1")
mydb.commit()
result=obj.fetchone()
print(result)

#DELETE DATA..........................
obj.execute("delete from student where id=1")
mydb.commit()
result=obj.fetchall()
for i in result:
    print(i)

#CLOSING..........................
obj.close()
mydb.close()