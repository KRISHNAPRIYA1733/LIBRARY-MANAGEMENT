class Father:
    def father_skills(self):
        print("Driving..")
class Mother:
    def mother_skills(self):
        print("Singing..")
class Child(Father,Mother):
    def child_skills(self):
        print("Dancing..")
obj=Child()
obj.child_skills()
obj.mother_skills()
obj.father_skills()
