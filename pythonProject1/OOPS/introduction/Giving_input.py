class student:
    def __init__(self):
        self.name=""
        self.Age=0
        self.Place=""
    def data(self):
        self.name=input("enter name:")
        self.Age=int(input("enter student age:"))
        self.Place=input("enter place:")
    def details(self):
        print("---student Details---")
        print("Name:",self.name)
        print("Place:",self.Place)
        print("Age:",self.Age)
obj1=student()
obj1.data()
obj1.details()