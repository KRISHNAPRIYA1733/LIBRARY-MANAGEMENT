from datetime import date
class Person:
    def __init__(self):
        self.name=""
        self.country=""
        self.dob=0
    def data(self):
        self.name=input("enter your name:")
        self.country=input("enter your country:")
        self.dob=int(input("enter your birth Year:"))
    def display(self):
        print("Name:",self.name)
        print("Country:",self.country)
        print("Date of birth:",self.dob)
    def age(self):
        year=date.today().year
        print("Age :",year-self.dob)
obj=Person()
obj.data()
obj.display()
obj.age()


