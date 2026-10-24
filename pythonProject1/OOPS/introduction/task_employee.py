class employee:
    def __init__(self,name,place,company,id,salary,designation):
        self.employee_name=name
        self.employee_place=place
        self.company_name=company
        self.company_id=id
        self.employee_salary=salary
        self.Designation=designation
    def display(self):
        print("...........Employee Details................")
        print("Name         :",self.employee_name)
        print("Place        :", self.employee_place)
        print("Company name :",   self.company_name)
        print("company id   :",self.company_id)
        print("Salary       :", self.employee_salary)
        print("Designation  :",self.Designation)
obj1=employee(name="Rahul",place="Kollam",company="Tcs",id=543,salary=30000,designation="developer")
obj1.display()
obj2=employee(name="Divya",place="kochi",company="Infosys",id=633,salary="25000",designation="Tester")
obj2.display()
obj3=employee(name="Anu",place="kottayam",company="Google",id=636,salary=50000,designation="analyst")
obj3.display()