import mysql.connector
class LibraryManagement:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Krishna@2005",
            database="librarydb"
        )
        print("connected successfully")
    def get(self):
        self.cursor=self.connection.cursor()
        query="select * from library"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for i in records:
            print(i)
    def get_one_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from library where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        self.cursor=self.connection.cursor()
        query="delete from library where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        self.connection.commit()
        print("deleted successfully")
    def post(self,**kwargs):
        self.cursor=self.connection.cursor()
        query="""
            insert into library(title,author,price)values(%s,%s,%s)"""
        values=[v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connection.commit()
        print("added successfully")
    def put(self,id=None,**kwargs):
        try:
            records=self.get_one_object(id=id)
            if id!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder +=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update library set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("updated successfully")
        except Exception as e:
            print(e)
library_instance=LibraryManagement()
#library_instance.post(title="Wings of Fire",author="A.P.J. Abdul Kalam",price=250)
#library_instance.get()
#library_instance.get_one_object(id=1)
#library_instance.delete(id=1)
library_instance.put(id=1,author="Kalam",price=300)