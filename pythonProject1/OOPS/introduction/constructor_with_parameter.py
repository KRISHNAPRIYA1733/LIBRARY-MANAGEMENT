class student:
    def __init__(self,name,course):
        self.student_name=name
        self.course_name=course
    def disply(self):
        print("student name:",self.student_name)
        print("course name:",self.course_name)
obj1=student("amal","Python")
obj1.disply()
