class Student:
    def __init__(self):
        self._marks=90
    def Sdisplay(self):
        print("Marks=",self._marks)
class Teacher(Student):
    def Tdisplay(self):
        print("---student details---")
        print("Student Mark",self._marks)
obj=Teacher()
obj.Sdisplay()
obj.Tdisplay()

print(obj._marks)     #This should not work.in protected only parent class and child class should be able to access the method