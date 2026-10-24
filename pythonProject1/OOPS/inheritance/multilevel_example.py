class Collage:
    def __init__(self):
        self.CollegeName=""
        self.Location=""
        self.number=0
    def collegedata(self):
        self.CollegeName=input("enter college name  :")
        self.Location=input("Enter college location:")
        self.number=int(input("enter collage number:"))
    def display(self):
        print("---college details-------")
        print("College Name:",self.CollegeName)
        print("College Location:",self.Location)
        print("Contact Number:",self.number)
class Department(Collage):
    def __init__(self):
        self.DeptID=0
        self.deptName=""
        self.HOD=""
    def DepData(self):
        self.deptName=input("enter department name:")
        self.DeptID=int(input("enter department id:"))
        self.HOD=input("enter HOD's name:")
    def DepDisplay(self):
        print("---department Details-----")
        print("Department Name:",self.deptName)
        print("Department Id:",self.DeptID)
        print("Department HOD:",self.HOD)
class Student(Department):
    def __init__(self):
        self.StuName=""
        self.stuID=0
        self.stuDep=""
        self.stuNum=0
    def stuData(self):
        self.StuName=input("Enter sudent Name:")
        self.stuID=int(input("Enter student ID:"))
        self.stuDep=input("enter department:")
        self.stuNum=int(input("enter phone number:"))
    def StuDisplay(self):
        print("----student details----")
        print("name:",self.StuName)
        print("ID:",self.stuID)
        print("Department:",self.stuDep)
        print("Number:",self.stuNum)
obj1=Student()
obj1.collegedata()
obj1.DepData()
obj1.stuData()
obj1.display()
obj1.DepDisplay()
obj1.StuDisplay()
