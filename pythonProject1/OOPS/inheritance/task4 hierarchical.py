class Company:
    def __init__(self):
        self.Name=""
        self.location=""
    def Cdata(self):
        self.Name=input("enter comapny name   :")
        self.location=input("enter company location:")
    def Cdisplay(self):
        print("------company details---------")
        print("Name     :",self.Name)
        print("Location :",self.location)
class Developer(Company):
    def __init__(self):
        self.name=""
        self.salary=""
    def Ddata(self):
        self.name = input("Enter name           :")
        self.salary = input("Enter salary:")
    def Ddisplay(self):
        print("------developer details---------")
        print("Name       :",self.name)
        print("salary     :",self.salary)
class Tester(Company):
    def __init__(self):
        self.name=""
        self.experience=""
    def Tdata(self):
        self.name = input("Enter name      :")
        self.experience = input("Enter experience  :")
    def Tdisplay(self):
        print("------Tester details---------")
        print("Name       :",self.name)
        print("Experience     :",self.experience)
class HR(Company):
    def __init__(self):
        self.name=""
        self.salary=""
    def Hdata(self):
        self.name = input("Enter name    :")
        self.salary = input("Enter salary:")
    def Hdisplay(self):
        print("Name       :",self.name)
        print("salary     :",self.salary)
class Manager(Company):
    def __init__(self):
        self.name=""
        self.experience = ""
    def Mdata(self):
        self.name = input("Enter name    :")
        self.experience = input("Enter experience  :")
    def Mdisplay(self):
        print("------Manager details---------")
        print("Name       :",self.name)
        print("Experience     :", self.experience)
obj1=Developer()
obj1.Cdata()
obj1.Ddata()
obj1.Cdisplay()
obj1.Ddisplay()

obj2=Tester()
obj2.Cdata()
obj2.Tdata()
obj2.Cdisplay()
obj2.Tdisplay()

obj4=HR()
obj4.Cdata()
obj4.Hdata()
obj4.Cdisplay()
obj4.Hdisplay()

obj5=Manager()
obj5.Cdata()
obj5.Mdata()
obj5.Cdisplay()
obj5.Mdisplay()