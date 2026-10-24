import mysql.connector
class FoodOrdering:
    def __init__(self):
        self.connection=mysql.connector.connect(host="localhost",user="root",password="Krishna@2005",database="fooddb")
        print("connected successfully!")
    def get(self):
        self.cursor=self.connection.cursor()
        query="select * from food"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        for i in records:
            print(i)
    def get_object(self,id=None):
        self.cursor=self.connection.cursor()
        query="select * from food where id=%s"
        value=(id,)
        self.cursor.execute(query,value)
        self.connection.commit()
        records=self.cursor.fetchone()
        return records
    def post(self,**kwargs):
        self.cursor=self.connection.cursor()
        query="""
            insert into food(name,price,category)
            values(%s,%s,%s)"""
        values=[v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connection.commit()
        print("updated successfully!")
    def delete(self,id=None):
        self.cursor=self.connection.cursor()
        query="delete from food where id=%s"
        value=(id,)
        self.cursor.execute(query,value)
        self.connection.commit()
        print("food deleted")
    def put(self,id=None,**kwargs):
        records=self.get_object(id=id)
        if records!=None:
            self.cursor=self.connection.cursor()
            placeholder=""
            for k in kwargs.keys():
                placeholder +=k+"=%s,"
            placeholder=placeholder.rstrip(",")
            query=f"update food set {placeholder} where id=%s"
            values=[v for v in kwargs.values()]
            values.append(id)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("updated successfully completed")

food_instance=FoodOrdering()
#food_instance.post(name="biriyani",price=250,category="main course")
#food_instance.get()
#food_instance.delete(id=3)
food_instance.put(id=1,name="amal",)