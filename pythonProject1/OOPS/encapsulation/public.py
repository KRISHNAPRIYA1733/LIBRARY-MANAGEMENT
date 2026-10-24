class Company:
    def __init__(self):
        self.Cname="Luminar"
    def Cdisplay(self):
        print("Company Name:",self.Cname)
class Employee(Company):
    def Edisplay(self):
        print("Company Name:",self.Cname)
obj=Company()
obj.Cdisplay()

obj1=Employee()
obj1.Edisplay()

print(obj1.Cname)
