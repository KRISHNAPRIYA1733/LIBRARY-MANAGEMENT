class Company:
    def __init__(self):
        self.companyName=""
        self.companyLocation=""
    def company_data(self):
        self.companyName=input("Enter company Name:")
        self.companyLocation=input("Enter company Location:")
    def Display(self):
        print("-----Company Details--------")
        print("Company Name        :",self.companyName)
        print("company Location    :",self.companyLocation)
class Employee(Company):
    def __init__(self):
        self.name=""
        self.id=0
        self.designation=""
        self.salary=0
    def Employee_data(self):
        self.name=input("Enter employee Name:")
        self.id=int(input("Enter employee id:"))
        self.designation=input("Enter your job role:")
        self.salary=int(input("Enter your salary:"))
    def Display_employee(self):
        print("-------Employee Details-------")
        print("Employee Name       :",self.name)
        print("Employee id         :",self.id)
        print("Employee's salary   :",self.salary)
        print("Employee Designation:",self.designation)
obj1=Employee()
obj1.company_data()
obj1.Employee_data()
obj1.Display()
obj1.Display_employee()