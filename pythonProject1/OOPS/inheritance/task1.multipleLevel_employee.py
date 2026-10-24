class Person:
    def __init__(self):
        self.name=""
        self.age=0
        self.place=""
        self.mobile=0
        self.email=""
    def Pdata(self):
        self.name=input("enter name    :")
        self.age=int(input("enter age  :"))
        self.place=input("enter palce  :")
        self.mobile=int(input("enter no:"))
        self.email=input("enter email  :")
    def Pdisplay(self):
        print("-----Person Details-----------")
        print("Enter Name             :",self.name)
        print("Enter Age              :",self.age)
        print("Enter Place            :",self.place)
        print("Enter Mobile number    :",self.mobile)
        print("Enter email            :",self.email)
class Salary:
    def __init__(self):
        self.base=0
        self.bonus=0
        self.doj=""
    def Sdata(self):
        self.base=int(input("enter base salary:"))
        self.bonus=int(input("enter bonus     :"))
        self.doj=input("enter date of joining :")
    def Sdisplay(self):
        print("-----Salary Details-----------")
        print("Base Salary            :",self.base)
        print("Bonus                  :",self.bonus)
        print("Date of Joining        :",self.doj)
class Employee(Person,Salary):
    def __init__(self):
        self.empID=0
        self.designation=""
    def Edata(self):
        self.empID=int(input("Enter employee id:"))
        self.designation=input("Enter job role :")
    def Edisplay(self):
        print("-----Employee Details-----------")
        print("Employee iD   :")
        print("Designation   :")
obj1=Employee()
obj1.Pdata()
obj1.Sdata()
obj1.Edata()
obj1.Pdisplay()
obj1.Sdisplay()
obj1.Edisplay()
