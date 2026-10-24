class Customer:
    def __init__(self):
        self.Name=""
        self.address=""
        self.mobile=0
        self.email=""
    def Cdata(self):
        self.Name=input("enter name:")
        self.address=input("enter address:")
        self.mobile=int(input("enter mobile number:"))
        self.email=input("enter email Id:")
    def Cdisplay(self):
        print("------customer details----------")
        print("Name           :",self.Name)
        print("Adress         :",self.address)
        print("mobile number  :",self.mobile)
        print("Email ID       :",self.email)
class Product:
    def __init__(self):
        self.pname=""
        self.price=""
        self.des=""
    def Pdata(self):
        self.pname=input("enter product name:")
        self.price=int(input("enter product price:"))
        self.des=input("enter product description")
    def Pdisplay(self):
        print("------product details----------")
        print("Product Name        :",self.pname)
        print("Price               :",self.price)
        print("Product Description :",self.des)
class Order(Customer,Product):
    def __init__(self):
        self.oid=0
        self.qty=0
        self.tp=0
        self.odate=""
    def Odata(self):
        self.oid=int(input("Enter orde id:"))
        self.qty=int(input("enter number of products:"))
        self.tp=int(input("enter total price:"))
        self.odate=input("enter order date:")
    def Odisplay(self):
        print("------order details----------")
        print("Order Id            :",self.oid)
        print("Quantity            :",self.qty)
        print("Total Price         :",self.tp)
        print("Order date          :",self.odate)
obj=Order()
obj.Cdata()
obj.Pdata()
obj.Odata()
obj.Cdisplay()
obj.Pdisplay()
obj.Odisplay()
