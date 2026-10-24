# class hospital
#     has name,location.contact
# class department
#     id,dep name,hod name
# class patient
#     pid,name,age,place,illness ,contact
class Hospital:
    def __init__(self):
        self.name=""
        self.loc=""
        self.contact=0
    def Hdata(self):
        self.name=input("enter hospital name:")
        self.loc=input("enter location:")
        self.contact=int(input("enter contact number:"))
    def Hdiplay(self):
        print("----hospital details--------")
        print("hospital name         :",self.name)
        print("Location              :",self.contact)
        print("Contact no            :",self.contact)
class Department(Hospital):
    def __init__(self):
        self.id=0
        self.dep=""
        self.hod=""
    def Ddata(self):
        obj.Hdata()
        self.id=int(input("Enter department id:"))
        self.dep=input("Enter department name:")
        self.hod=input("Enter hod name:")
    def Ddisplay(self):
        obj.Hdiplay()
        print("----Department details--------")
        print("Department Id          :",self.id)
        print("Department Name        :",self.dep)
        print("HOD                    :",self.hod)
class Patient(Department):
    def __init__(self):#     pid,name,age,place,illness ,contact
        self.pid=0
        self.Pname=""
        self.age=0
        self.place=""
        self.ill=""
        self.cont=0
    def Pdata(self):
        obj.Ddata()
        self.pid=int(input("enter patient id:"))
        self.Pname=input("enter patient name:")
        self.age=int(input("enter age:"))
        self.place=input("enter place:")
        self.ill=input("enter illness:")
        self.cont=int(input("enter contact number:"))
    def Pdisplay(self):
        obj.Ddisplay()
        print("----Patient details--------")
        print("Patient id          :",self.pid)
        print("patient Name        :",self.Pname)
        print("Age                 :",self.age)
        print("Place               :",self.place)
        print("Illness             :",self.ill)
        print("Contact number      :",self.cont)
obj=Patient()
obj.Pdata()
obj.Pdisplay()