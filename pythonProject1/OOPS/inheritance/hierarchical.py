class Employee:
    def Company(self):
        print("Company Name : Luminar")
class Manager(Employee):
    def manage(self):
        print("Manager manages the comapany")
class Developer(Employee):
    def code(self):
        print("Developers writes code")
obj1=Manager()
obj1.Company()
obj1.manage()

obj3=Developer()
obj3.Company()
obj3.code()