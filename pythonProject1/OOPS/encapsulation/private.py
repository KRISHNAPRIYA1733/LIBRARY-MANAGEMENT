class Employee:
    def __init__(self):
        self.name="Arya"
        self.__salary=30000
    def Display(self):
        print("Name:",self.name)
        print("Salary:",self.__salary)
obj=Employee()
obj.Display()
print("outside class.....")
print(obj.name)
print(obj.__salary)