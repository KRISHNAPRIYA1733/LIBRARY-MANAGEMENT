class Grandfather:
    def car(self):
        print("Grandfather's car!")
class Father(Grandfather):
    def bike(self):
        print("Father's bike")
class Son(Father):
    def laptop(self):
        print("son's laptop!")
obj=Son()
obj.laptop()
obj.bike()
obj.car()